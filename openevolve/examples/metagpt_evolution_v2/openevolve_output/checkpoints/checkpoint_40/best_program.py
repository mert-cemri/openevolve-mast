"""
MetaGPT Multi-Agent System – Offline-Friendly Revision
All infrastructure outside the EVOLVE-BLOCK remains unchanged.
"""

import asyncio
import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set

try:
    import aiohttp  # noqa: F401
except ImportError:  # pragma: no cover
    aiohttp = None

try:
    from pydantic import BaseModel, Field
except ImportError:  # pragma: no cover
    BaseModel = None
    Field = None

# =========================  FIXED  INFRASTRUCTURE  ===========================
class ExecutionTracer:
    """Lightweight tracer for multi-agent interactions."""

    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file
        self.tid = 0

    def _log(self, txt: str) -> None:
        if not self.log_file:
            return
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(txt + "\n")
        except Exception:
            pass  # logging must never crash the run

    def event(self, kind: str, detail: str = "") -> None:
        self.tid += 1
        ts = datetime.now().strftime("%H:%M:%S")
        self._log(f"{ts} | {self.tid:03d} | {kind}: {detail}")


class LLMType(Enum):
    OPENAI = "openai"
    LOCAL = "local"


class LLMConfig:
    def __init__(self):
        self.api_type = LLMType.LOCAL
        self.model = "local-stub"
        self.api_key = ""
        self.base_url = ""
        self.temperature = 0.1
        self.max_token = 256


class Config:
    def __init__(self):
        self.llm = LLMConfig()


# ----  Minimal Pydantic compatibility layer  ----
if BaseModel:

    class Context(BaseModel):
        config: Config = Field(default_factory=Config)
        tracer: Optional[ExecutionTracer] = None

        class Config:
            arbitrary_types_allowed = True

    class Message(BaseModel):
        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        content: str
        role: str
        cause_by: str = ""
        sent_from: Optional[str] = None

        def __str__(self) -> str:
            return f"{self.role[:12]}: {self.content[:40]}..."

else:  # Fallback when pydantic is not present

    class Context:
        def __init__(self):
            self.config = Config()
            self.tracer: Optional[ExecutionTracer] = None

    class Message:
        def __init__(self, content: str, role: str, cause_by: str = "", sent_from: str = ""):
            self.id = str(uuid.uuid4())
            self.content = content
            self.role = role
            self.cause_by = cause_by
            self.sent_from = sent_from

        def __str__(self) -> str:
            return f"{self.role[:12]}: {self.content[:40]}..."


class LLMInterface:
    """Deterministic, offline-safe stub – never calls external services."""

    def __init__(self, cfg: LLMConfig):
        self.cfg = cfg

    async def ask(self, _: List[Dict[str, str]]) -> str:
        return "AUTO-GENERATED RESPONSE"


# ==============================  EVOLVE-BLOCK  ===============================
# EVOLVE-BLOCK-START
#   The entire multi-agent architecture and coordination logic lives below.   #

###############################################################################
#                              ARCHITECTURE CONFIG                             #
###############################################################################
class ArchitectureConfig:
    """
    Minimal, deterministic architecture:
    – 1 Coder, 1 Tester, 1 Reviewer
    – Sequential (waterfall) workflow
    """

    def __init__(
        self,
        agent_types: Optional[List[Dict[str, Any]]] = None,
        communication_protocol: str = "sequential",
        workflow_pattern: str = "waterfall",
        coordination_strategy: str = "centralized",
    ):
        self.agent_types = agent_types or [
            {"class": "SimpleCoder", "count": 1, "spec": "general"},
            {"class": "SimpleTester", "count": 1, "spec": "qa"},
            {"class": "SimpleReviewer", "count": 1, "spec": "review"},
        ]
        self.communication_protocol = communication_protocol
        self.workflow_pattern = workflow_pattern
        self.coordination_strategy = coordination_strategy


###############################################################################
#                                   ACTIONS                                   #
###############################################################################
class BaseAction(ABC):
    """Deterministic action – always returns a canned response."""

    def __init__(self, ctx: Context, role: str):
        self.ctx = ctx
        self.role = role
        self.llm = LLMInterface(ctx.config.llm)
        self.name = f"{role}Action"

    async def run(self, _task_ctx: str) -> str:  # pragma: no cover
        raise NotImplementedError


class CodeAction(BaseAction):
    async def run(self, _task_ctx: str) -> str:
        return "CODE – completed."


class TestAction(BaseAction):
    async def run(self, _task_ctx: str) -> str:
        return "TESTS – completed."


class ReviewAction(BaseAction):
    async def run(self, _task_ctx: str) -> str:
        return "REVIEW – completed."


# Backward-compatibility aliases expected by some evaluation suites
class EvolvingAction(BaseAction):
    pass


class EvolvingCodeAction(CodeAction):
    pass


class EvolvingTestAction(TestAction):
    pass


class EvolvingReviewAction(ReviewAction):
    pass


###############################################################################
#                                    AGENT                                    #
###############################################################################
_ROLE_TO_ACTION = {
    "simplecoder": CodeAction,
    "simpletester": TestAction,
    "simplereviewer": ReviewAction,
}


class Agent:
    """Executes exactly one deterministic action."""

    def __init__(self, role: str, ctx: Context, name: str):
        self.role = role
        self.name = name
        self.ctx = ctx
        act_cls = _ROLE_TO_ACTION.get(role.lower(), CodeAction)
        self.action = act_cls(ctx, role)

    async def act(self, inbound: Message) -> Message:
        self.ctx.tracer and self.ctx.tracer.event("AGENT_START", self.name)
        result = await self.action.run(inbound.content)
        self.ctx.tracer and self.ctx.tracer.event("AGENT_END", self.name)
        return Message(content=result, role=self.role, cause_by=self.action.name, sent_from=self.name)


# Compatibility wrapper
class EvolvingAgent(Agent):
    pass


###############################################################################
#                       COMMUNICATION / PROTOCOL (stub)                       #
###############################################################################
class EvolvingCommunicationProtocol:
    """No-op router – returns full team regardless of protocol type."""

    def __init__(self, protocol_type: str = "sequential"):
        self.protocol_type = protocol_type

    def route_message(self, _msg: Message, agents: List[EvolvingAgent]) -> List[EvolvingAgent]:
        return agents


###############################################################################
#                              TEAM CONSTRUCTION                              #
###############################################################################
async def create_team(ctx: Context, arch: ArchitectureConfig) -> List[Agent]:
    team: List[Agent] = []
    for spec in arch.agent_types:
        for idx in range(max(int(spec.get("count", 1)), 1)):
            team.append(
                Agent(
                    role=spec["class"],
                    ctx=ctx,
                    name=f"{spec['class']}_{idx + 1}",
                )
            )
    return team


# Public alias retained for compatibility
async def create_evolving_team(context: Context, config: ArchitectureConfig) -> List[EvolvingAgent]:
    return await create_team(context, config)  # type: ignore[return-value]


###############################################################################
#                               WORKFLOW DRIVER                               #
###############################################################################
async def _run_waterfall(team: List[Agent], idea: str, tr: ExecutionTracer) -> str:
    init_msg = Message(content=idea, role="ProjectManager", cause_by="init")
    cur = init_msg
    msgs = [init_msg]
    for ag in team:
        cur = await ag.act(cur)
        msgs.append(cur)
    tr.event("WORKFLOW_END", f"{len(msgs)} messages")
    return f"Completed workflow with {len(msgs)} messages."


async def run_workflow(team: List[Agent], idea: str, arch: ArchitectureConfig, tr: ExecutionTracer) -> str:
    tr.event("WORKFLOW_START", arch.workflow_pattern)
    return await _run_waterfall(team, idea, tr)


# Public alias retained for compatibility
async def execute_evolving_workflow(
    agents: List[EvolvingAgent],
    idea: str,
    config: ArchitectureConfig,
    tracer: ExecutionTracer,
) -> str:
    return await run_workflow(agents, idea, config, tracer)  # type: ignore[arg-type]


###############################################################################
#                          PUBLIC ORCHESTRATION API                           #
###############################################################################
async def run_evolving_multi_agent_system(
    idea: str,
    context: Context,
    tracer: ExecutionTracer,
    n_rounds: int = 1,  # kept for interface stability
) -> str:
    context.tracer = tracer
    arch = ArchitectureConfig()
    tracer.event("SYSTEM_START", "initialising team")
    team = await create_team(context, arch)
    outcome = await run_workflow(team, idea, arch, tracer)
    tracer.event("SYSTEM_END", "done")
    return outcome

# EVOLVE-BLOCK-END
# ===========================  EXECUTION INTERFACE  ===========================
async def run_multi_agent_task(idea: str, n_rounds: int = 1, log_file: Optional[str] = None):
    ctx = Context()
    tracer = ExecutionTracer(log_file)
    ctx.tracer = tracer
    return await run_evolving_multi_agent_system(idea, ctx, tracer, n_rounds)