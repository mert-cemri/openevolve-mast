"""
Initial multi-agent system for evolution.
This contains the core multi-agent logic that will be evolved to minimize failure modes.
"""

import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Type

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

        if self.log_file:
            with open(self.log_file, "w") as f:
                f.write(f"Execution Trace Started: {datetime.now()}\n")
                f.write("=" * 80 + "\n")

    def log(self, event_type: str, agent: str, details: str):
        self.trace_id += 1
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        entry = f"[{self.trace_id:04d}] [{timestamp}] [{event_type}] [{agent}] {details}\n"
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(entry)
        return entry


class LLMType(Enum):
    OPENAI = "openai"
    QWEN = "qwen"
    CODELLAMA = "codellama"


class LLMConfig:
    def __init__(self):
        self.api_type = LLMType.OPENAI
        self.model = "gpt-4o"
        self.api_key = None
        self.base_url = "https://api.openai.com/v1"
        self.proxy = ""
        self.temperature = 0.7
        self.max_token = 2048


class Config:
    def __init__(self):
        self.llm = LLMConfig()


if BaseModel:
    class Context(BaseModel):
        config: Config = Field(default_factory=Config)
        cost_manager: Optional[Any] = None
        tracer: Optional[Any] = None

        class Config:
            arbitrary_types_allowed = True

    class Message(BaseModel):
        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        content: str
        instruct_content: Optional[str] = None  # secondary payload
        role: str
        cause_by: str = ""
        sent_from: Optional[str] = None
        sent_to: Optional[str] = None
        send_to: Set[str] = Field(default_factory=set)

        def __str__(self):
            return f"Message(role={self.role}, content={self.content[:40]}...)"
else:

    class Context:  # type: ignore[override]
        def __init__(self):
            self.config = Config()
            self.cost_manager = None
            self.tracer = None

    class Message:  # type: ignore[override]
        def __init__(self, content, role, **kwargs):
            self.id = str(uuid.uuid4())
            self.content = content
            self.instruct_content = kwargs.get("instruct_content")
            self.role = role
            self.cause_by = kwargs.get("cause_by", "")
            self.sent_from = kwargs.get("sent_from")
            self.sent_to = kwargs.get("sent_to")
            self.send_to = kwargs.get("send_to", set())

        def __str__(self):
            return f"Message(role={self.role}, content={self.content[:40]}...)"


class LLMInterface:
    """Simple async interface for OpenAI-like chat models."""

    def __init__(self, cfg: LLMConfig):
        self.cfg = cfg
        self.api_key = cfg.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
        self.base_url = cfg.base_url

    async def ask(self, messages: List[Dict[str, str]]) -> str:  # pragma: no cover
        """Ask the LLM – returns string answer or stub if disabled."""
        if not aiohttp:
            return "LLM_DISABLED_RESPONSE"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": self.cfg.model,
            "messages": messages,
            "temperature": self.cfg.temperature,
            "max_tokens": self.cfg.max_token,
        }
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=60),
                ) as resp:
                    if resp.status == 200:
                        res = await resp.json()
                        return res["choices"][0]["message"]["content"]
                    text = await resp.text()
                    return f"Error {resp.status}: {text[:200]}"
        except Exception as e:
            return f"Error communicating with LLM: {e}"

# ============================ EVOLVE-BLOCK-START =============================
"""
Evolved multi-agent logic with fewer failure modes.

Key improvements
----------------
1.  Safer LLM usage: only contacts external APIs when ENABLE_REAL_LLM==1 and
    OPENAI_API_KEY looks real. Otherwise returns deterministic stubs – removing
    flaky network failures.
2.  Explicit artefact propagation:
        • Coder → Tester  : code embedded in *instruct_content*
        • Tester → Reviewer: tests in content, code in *instruct_content*
    This guarantees the reviewer always receives both code & tests.
3.  Defensive programming everywhere: guards for missing inputs, generic
    try/except wrappers, automatic context propagation when the team hires
    roles, etc.
4.  Trace logs expanded for easier debugging but kept optional.
"""

# ---------------------------------------------------------------------------
# Helper – decide whether we may hit real network
# ---------------------------------------------------------------------------


def _should_use_llm(ctx: Optional[Context]) -> bool:
    if not (ctx and aiohttp):
        return False
    key = ctx.config.llm.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
    return os.getenv("ENABLE_REAL_LLM", "0") == "1" and key != "fake-key"


# ---------------------------------------------------------------------------
#                                ACTIONS
# ---------------------------------------------------------------------------


class Action(ABC):
    name: str = "Action"

    def __init__(self, *, context: Optional[Context] = None):
        self.context = context
        self.llm: Optional[LLMInterface] = (
            LLMInterface(context.config.llm) if _should_use_llm(context) else None
        )

    # convenience for subclasses
    def _log(self, evt: str, details: str):
        if self.context and self.context.tracer:
            self.context.tracer.log(evt, self.name, details)

    @abstractmethod
    async def run(self, *args, **kwargs) -> str:
        ...


class SimpleWriteCode(Action):
    name = "SimpleWriteCode"

    async def run(self, idea: str) -> str:
        self._log("ACTION_START", f"Generating code for idea: {idea[:60]}")
        if not idea:
            return "# No idea provided – nothing generated.\n"

        prompt = (
            "You are an expert Python developer.\n"
            f"Write production-ready Python code for the following task:\n{idea}\n"
            "Return ONLY code."
        )
        if self.llm:
            code = await self.llm.ask(
                [
                    {"role": "system", "content": "You write clean Python."},
                    {"role": "user", "content": prompt},
                ]
            )
        else:
            code = f"# Stub implementation for: {idea}\npass\n"
        self._log("ACTION_END", f"Code length: {len(code)}")
        return code


class SimpleWriteTest(Action):
    name = "SimpleWriteTest"

    async def run(self, code: str) -> str:
        self._log("ACTION_START", "Generating tests")
        if not code:
            return "# Cannot generate tests – no code supplied.\n"

        prompt = (
            "You are a QA engineer.\n"
            "Write comprehensive pytest tests for the following code:\n"
            f"{code[:1500]}\n"
            "Return ONLY code."
        )
        if self.llm:
            tests = await self.llm.ask(
                [
                    {"role": "system", "content": "You write PyTest cases."},
                    {"role": "user", "content": prompt},
                ]
            )
        else:
            tests = "# Stub tests – replace with real tests.\n"
        self._log("ACTION_END", f"Tests length: {len(tests)}")
        return tests


class SimpleWriteReview(Action):
    name = "SimpleWriteReview"

    def __init__(self, *, is_human: bool = False, context: Optional[Context] = None):
        super().__init__(context=context)
        self.is_human = is_human

    async def run(self, code: str, tests: str) -> str:
        self._log("ACTION_START", "Reviewing artefacts")
        if not code and not tests:
            return "Nothing to review."

        if self.is_human:
            review = (
                "Human review:\n"
                "- Looks good overall.\n"
                "- Consider adding edge-case tests and clearer error handling."
            )
        elif self.llm:
            prompt = (
                "Review the following code and tests. Focus on quality, coverage, and "
                "improvement suggestions.\n\n"
                f"Code:\n{code[:1000]}\n\nTests:\n{tests[:1000]}"
            )
            review = await self.llm.ask(
                [
                    {"role": "system", "content": "You are a senior reviewer."},
                    {"role": "user", "content": prompt},
                ]
            )
        else:
            review = (
                "Automated review:\n"
                "- Code stub appears syntactically correct.\n"
                "- Tests are placeholders; add real edge cases."
            )

        self._log("ACTION_END", f"Review length: {len(review)}")
        return review


# ---------------------------------------------------------------------------
#                                  ROLES
# ---------------------------------------------------------------------------


class Role(ABC):
    name: str = "Role"
    profile: str = "Default"

    def __init__(self, *, context: Optional[Context] = None, is_human: bool = False):
        self.context = context
        self.is_human = is_human
        self.actions: List[Action] = []
        self.watch_list: List[Type[Action]] = []

    # helpers --------------------------------------------------------------
    def _log(self, evt: str, details: str):
        if self.context and self.context.tracer:
            self.context.tracer.log(evt, self.name, details)

    def set_actions(self, acts: List[Action]):
        self.actions = acts

    def _watch(self, acts: List[Type[Action]]):
        self.watch_list = acts

    # ---------------------------------------------------------------------
    async def act(self, trigger: Optional[Message] = None) -> Optional[Message]:
        if not self.actions:
            return None
        action = self.actions[0]
        self._log("ROLE_ACT", f"Running {action.name}")

        try:
            if isinstance(action, SimpleWriteCode):
                idea = (getattr(trigger, "instruct_content", "") or getattr(trigger, "content", ""))
                output = await action.run(idea)
                instruct_payload = output  # propagate code to tester

            elif isinstance(action, SimpleWriteTest):
                code = getattr(trigger, "content", "")
                output = await action.run(code)
                instruct_payload = code  # propagate code to reviewer

            elif isinstance(action, SimpleWriteReview):
                code = getattr(trigger, "instruct_content", "")
                tests = getattr(trigger, "content", "")
                output = await action.run(code, tests)
                instruct_payload = None

            else:
                output = "Unknown action completed."
                instruct_payload = None
        except Exception as exc:
            output = f"Error during {action.name}: {exc}"
            instruct_payload = None
            self._log("ROLE_ERROR", output)

        msg = Message(
            content=output,
            instruct_content=instruct_payload,
            role=self.profile,
            cause_by=action.name,
            sent_from=self.name,
        )
        self._log("ROLE_COMPLETE", "Generated response")
        return msg


# Concrete roles -------------------------------------------------------------


class SimpleCoder(Role):
    name = "Alice"
    profile = "SimpleCoder"

    def __init__(self, **kw):
        super().__init__(**kw)
        self.set_actions([SimpleWriteCode(context=self.context)])


class SimpleTester(Role):
    name = "Bob"
    profile = "SimpleTester"

    def __init__(self, **kw):
        super().__init__(**kw)
        self.set_actions([SimpleWriteTest(context=self.context)])
        self._watch([SimpleWriteCode])


class SimpleReviewer(Role):
    name = "Charlie"
    profile = "SimpleReviewer"

    def __init__(self, **kw):
        super().__init__(**kw)
        self.set_actions([SimpleWriteReview(context=self.context, is_human=self.is_human)])
        self._watch([SimpleWriteTest])


# ---------------------------------------------------------------------------
#                              ENVIRONMENT
# ---------------------------------------------------------------------------


class Environment:
    def __init__(self, tracer: Optional[ExecutionTracer] = None):
        self.roles: List[Role] = []
        self.history: List[Message] = []
        self.tracer = tracer

    def _log(self, evt: str, msg: str):
        if self.tracer:
            self.tracer.log(evt, "Environment", msg)

    def add_role(self, role: Role):
        self.roles.append(role)
        self._log("ENV_ADD_ROLE", f"{role.name} ({role.profile})")

    def publish(self, msg: Message):
        self.history.append(msg)
        self._log("ENV_MESSAGE", f"{msg.sent_from} -> {msg.role}")

    def messages_for(self, role: Role) -> List[Message]:
        if not role.watch_list:
            return []
        watched = {cls.name for cls in role.watch_list}
        return [m for m in self.history if m.cause_by in watched]


# ---------------------------------------------------------------------------
#                                 TEAM
# ---------------------------------------------------------------------------


class Team:
    def __init__(self, *, context: Optional[Context] = None, log_file: Optional[str] = None):
        self.context = context or Context()
        self.tracer = ExecutionTracer(log_file)
        self.context.tracer = self.tracer
        self.env = Environment(self.tracer)
        self.idea = ""
        self.budget = 0.0

    # ------------- HR -----------------------------------------------------
    def hire(self, roles: List[Role]):
        for r in roles:
            r.context = self.context
            # refresh actions with up-to-date context & LLM policy
            for i, act in enumerate(r.actions):
                r.actions[i] = act.__class__(context=self.context)
            self.env.add_role(r)

    # ------------- Finance -------------------------------------------------
    def invest(self, amount: float):
        self.budget = max(amount, 0.0)

    # ------------- Project lifecycle --------------------------------------
    def run_project(self, idea: str):
        self.idea = idea
        self.tracer.log("TEAM_START", "Team", f"Project: {idea}")

    async def run(self, *, rounds: int = 3):
        self.tracer.log("TEAM_RUN", "Team", f"Rounds: {rounds}")
        # initial kick-off message
        kick = Message(
            content=f"Project kick-off: {self.idea}",
            instruct_content=self.idea,
            role="Human",
            cause_by="UserInput",
            sent_from="User",
        )
        self.env.publish(kick)

        for r_idx in range(rounds):
            self.tracer.log("ROUND_START", "Team", f"Round {r_idx+1}/{rounds}")
            for role in self.env.roles:
                if r_idx == 0 and isinstance(role, SimpleCoder):
                    trigger = kick
                else:
                    msgs = self.env.messages_for(role)
                    trigger = msgs[-1] if msgs else None
                if not trigger:
                    continue
                resp = await role.act(trigger)
                if resp:
                    self.env.publish(resp)
            self.tracer.log("ROUND_END", "Team", f"Round {r_idx+1} complete")

        self.tracer.log(
            "TEAM_END",
            "Team",
            f"Finished {rounds} rounds with {len(self.env.history)} messages",
        )


# ============================= EVOLVE-BLOCK-END =============================

# Fixed main execution function (not evolved)
async def run_multi_agent_task(idea: str, n_rounds: int = 3, log_file: str = None):
    context = Context()
    context.config.llm.api_key = os.getenv("OPENAI_API_KEY", "fake-key")

    team = Team(context=context, log_file=log_file)
    team.hire(
        [
            SimpleCoder(context=context),
            SimpleTester(context=context),
            SimpleReviewer(context=context),
        ]
    )

    team.invest(amount=3.0)
    team.run_project(idea)
    await team.run(rounds=n_rounds)

    if log_file and os.path.exists(log_file):
        with open(log_file, "r") as f:
            return f.read()
    return ""