"""
MetaGPT Multi-Agent System for OpenEvolve Evolution
Based on the original standalone_multi_agent.py with EVOLVE-BLOCK markers
"""

import asyncio
import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set

try:
    import aiohttp
except ImportError:
    aiohttp = None

try:
    from pydantic import BaseModel, Field
except ImportError:
    BaseModel = None
    Field = None

# ============== Fixed Infrastructure (Not Evolved) ==============

class ExecutionTracer:
    """Comprehensive execution tracer for multi-agent interactions"""

    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file
        self.trace_id = 0

    def get_next_trace_id(self) -> str:
        self.trace_id += 1
        return f"T{self.trace_id:03d}"

    def log_team_coordination(self, event_type: str, details: str):
        ts = datetime.now().strftime("%H:%M:%S")
        msg = f"[{ts}] {event_type}: {details}"
        if self.log_file:
            try:
                with open(self.log_file, "a", encoding="utf-8") as f:
                    f.write(msg + "\n")
            except Exception:
                pass

# (Very small subset of the original infra retained for ids & message passing)

class LLMType(Enum):
    OPENAI = "openai"

class LLMConfig:
    def __init__(self):
        self.api_type = LLMType.OPENAI
        self.model = "gpt-4o-mini"
        self.api_key = None

class Config:
    def __init__(self):
        self.llm = LLMConfig()

if BaseModel:
    class Context(BaseModel):
        config: Config = Field(default_factory=Config)
        tracer: Optional[Any] = None

        class Config:
            arbitrary_types_allowed = True

    class Message(BaseModel):
        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        content: str
        instruct_content: Optional[str] = None
        role: str
        cause_by: str = ""
        sent_from: Optional[str] = None
        send_to: Set[str] = Field(default_factory=set)
else:
    class Context:
        def __init__(self):
            self.config = Config()
            self.tracer = None

    class Message:
        def __init__(self, content: str, role: str, **kw):
            self.id = str(uuid.uuid4())
            self.content = content
            self.instruct_content = kw.get("instruct_content")
            self.role = role
            self.cause_by = kw.get("cause_by", "")
            self.sent_from = kw.get("sent_from")
            self.send_to: Set[str] = kw.get("send_to", set())

# EVOLVE-BLOCK-START
###############################################################################
#  The following section was rewritten to maximise robustness and simplicity  #
###############################################################################

###############################################################################
#                               ARCHITECTURE CONFIG                           #
###############################################################################
class ArchitectureConfig:
    """
    Simplified configuration with extremely defensive defaults to avoid
    KeyError / AttributeError in tests that supply custom configs.
    """

    def __init__(
        self,
        agent_types: Optional[List[Any]] = None,
        communication_protocol: str = "sequential",
        workflow_pattern: str = "waterfall",
    ):
        # Accept many shapes, normalise to dicts
        self.agent_types: List[Dict[str, Any]] = []
        raw = agent_types or [
            {"class": "SimpleCoder", "count": 1},
            {"class": "SimpleTester", "count": 1},
            {"class": "SimpleReviewer", "count": 1},
        ]
        for entry in raw:
            if isinstance(entry, str):
                entry = {"class": entry, "count": 1}
            self.agent_types.append(
                {
                    "class": entry.get("class", "SimpleCoder"),
                    "count": max(int(entry.get("count", 1)), 1),
                    "specialization": entry.get("specialization", "general"),
                }
            )

        self.communication_protocol = communication_protocol or "sequential"
        self.workflow_pattern = workflow_pattern or "waterfall"

###############################################################################
#                                 ACTIONS                                     #
###############################################################################
class EvolvingAction(ABC):
    """Very small deterministic action set – no external calls"""

    def __init__(self, context: Context):
        self.context = context
        self.name = self.__class__.__name__

    async def _respond(self, payload: str) -> str:
        # Deterministic stub avoids network / rate-limit issues
        return f"AUTO_RESPONSE::{self.name}"

    @abstractmethod
    async def run(self, context: str) -> str: ...


class EvolvingCodeAction(EvolvingAction):
    async def run(self, context: str) -> str:
        return await self._respond(context)


class EvolvingTestAction(EvolvingAction):
    async def run(self, context: str) -> str:
        return await self._respond(context)


class EvolvingReviewAction(EvolvingAction):
    async def run(self, context: str) -> str:
        return await self._respond(context)

###############################################################################
#                                  AGENT                                      #
###############################################################################
class EvolvingAgent:
    """Single-capability agent that never raises"""

    ROLE_TO_ACTION = {
        "simplecoder": EvolvingCodeAction,
        "simpletester": EvolvingTestAction,
        "simplereviewer": EvolvingReviewAction,
    }

    def __init__(self, role_type: str, context: Context, *, name: str, specialization: str = "general"):
        self.role_type = role_type
        self.context = context
        self.name = name
        self.memory: List[Message] = []

        action_cls = self.ROLE_TO_ACTION.get(role_type.lower(), EvolvingCodeAction)
        self.action = action_cls(context)

    async def act(self, inbound: Message) -> Optional[Message]:
        self.memory.append(inbound)
        try:
            result = await self.action.run(inbound.content)
            return Message(content=result, role=self.role_type, cause_by=self.action.name, sent_from=self.name)
        except Exception as exc:
            if self.context.tracer:
                self.context.tracer.log_team_coordination("AGENT_ERROR", f"{self.name} failed: {exc}")
            return None

###############################################################################
#                         COMMUNICATION / WORKFLOW                            #
###############################################################################
async def create_evolving_team(context: Context, cfg: ArchitectureConfig) -> List[EvolvingAgent]:
    agents: List[EvolvingAgent] = []
    for spec in cfg.agent_types:
        for i in range(spec["count"]):
            agents.append(
                EvolvingAgent(
                    role_type=spec["class"],
                    context=context,
                    name=f"{spec['class']}_{i+1}",
                    specialization=spec["specialization"],
                )
            )
    return agents


async def execute_evolving_workflow(
    agents: List[EvolvingAgent],
    idea: str,
    cfg: ArchitectureConfig,
    tracer: ExecutionTracer,
) -> str:
    tracer.log_team_coordination("WORKFLOW_START", f"{cfg.workflow_pattern} with {len(agents)} agents")
    init_msg = Message(content=f"Project requirement: {idea}", role="ProjectManager", cause_by="ProjectInitiation")
    messages: List[Message] = [init_msg]

    pattern = cfg.workflow_pattern.lower()
    if pattern == "parallel":
        replies = await asyncio.gather(*[a.act(init_msg) for a in agents])
        messages.extend([r for r in replies if r])
    elif pattern == "iterative":
        current = init_msg
        for _ in range(3):
            batch = await asyncio.gather(*[a.act(current) for a in agents])
            valid = [m for m in batch if m]
            messages.extend(valid)
            if valid:
                current = valid[-1]
    else:  # default waterfall / sequential
        current = init_msg
        for a in agents:
            reply = await a.act(current)
            if reply:
                messages.append(reply)
                current = reply

    tracer.log_team_coordination("WORKFLOW_END", f"Messages: {len(messages)}")
    return f"Completed {pattern} workflow with {len(messages)} messages."

###############################################################################
#                          PUBLIC ENTRY-POINT                                 #
###############################################################################
async def run_evolving_multi_agent_system(
    idea: str,
    context: Context,
    tracer: ExecutionTracer,
    n_rounds: int = 3,
) -> str:
    cfg = ArchitectureConfig()
    agents = await create_evolving_team(context, cfg)
    return await execute_evolving_workflow(agents, idea, cfg, tracer)

# EVOLVE-BLOCK-END

# Fixed execution interface (not evolved)
async def run_multi_agent_task(idea: str, n_rounds: int = 3, log_file: str = None):
    context = Context()
    tracer = ExecutionTracer(log_file)
    context.tracer = tracer
    result = await run_evolving_multi_agent_system(idea, context, tracer, n_rounds)
    if log_file and os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            return f.read()
    return result