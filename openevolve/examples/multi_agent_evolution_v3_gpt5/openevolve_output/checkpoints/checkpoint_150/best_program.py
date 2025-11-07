# python
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
            # Clear the log file at the start
            with open(self.log_file, 'w') as f:
                f.write(f"Execution Trace Started: {datetime.now()}\n")
                f.write("="*80 + "\n")
    
    def log(self, event_type: str, agent: str, details: str):
        """Log an event to the trace file"""
        self.trace_id += 1
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        log_entry = f"[{self.trace_id:04d}] [{timestamp}] [{event_type}] [{agent}] {details}\n"
        
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        
        return log_entry

class LLMType(Enum):
    """LLM types"""
    OPENAI = "openai"
    QWEN = "qwen"
    CODELLAMA = "codellama"

class LLMConfig:
    """LLM configuration"""
    def __init__(self):
        self.api_type = LLMType.OPENAI
        self.model = "gpt-5"
        self.api_key = None
        self.base_url = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
        self.proxy = ""
        self.temperature = 0.35
        self.max_token = 8192

class Config:
    """Configuration object"""
    def __init__(self):
        self.llm = LLMConfig()

if BaseModel:
    class Context(BaseModel):
        """Context object that holds configuration and shared state"""
        config: Config = Field(default_factory=Config)
        cost_manager: Optional[Any] = None
        tracer: Optional[Any] = None
        
        class Config:
            arbitrary_types_allowed = True
    
    class Message(BaseModel):
        """Message object for agent communication"""
        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        content: str
        instruct_content: Optional[str] = None
        role: str
        cause_by: str = ""
        sent_from: Optional[str] = None
        sent_to: Optional[str] = None
        send_to: Set[str] = Field(default_factory=set)
        
        def __str__(self):
            return f"Message(role={self.role}, content={self.content[:50]}...)"
else:
    # Fallback classes if pydantic is not available
    class Context:
        def __init__(self):
            self.config = Config()
            self.cost_manager = None
            self.tracer = None
    
    class Message:
        def __init__(self, content, role, **kwargs):
            self.id = str(uuid.uuid4())
            self.content = content
            self.instruct_content = kwargs.get('instruct_content')
            self.role = role
            self.cause_by = kwargs.get('cause_by', '')
            self.sent_from = kwargs.get('sent_from')
            self.sent_to = kwargs.get('sent_to')
            self.send_to = kwargs.get('send_to', set())

class LLMInterface:
    """Interface for LLM communication"""
    def __init__(self, config: LLMConfig):
        self.config = config
        self.api_key = config.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
        self.base_url = config.base_url
    
    async def ask(self, messages: List[Dict[str, str]]) -> str:
        """Send messages to LLM and get response"""
        if not aiohttp:
            # Fallback for testing without actual API calls
            return "I'll help you with that task. Let me write the code for you."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.config.model,
            "messages": messages,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_token
        }
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=120)) as session:
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result["choices"][0]["message"]["content"]
                    else:
                        error_text = await response.text()
                        return f"Error: {response.status} - {error_text[:200]}"
        except Exception as e:
            return f"Error communicating with LLM: {str(e)}"

# EVOLVE-BLOCK-START
# This section contains the multi-agent system logic that will be evolved

import asyncio
import time
import ast
from typing import Tuple

# Evolution goals:
# - Clear role responsibilities
# - Robust inter-agent communication with explicit routing (send_to) and watch/trigger logic
# - Deterministic orchestration and processed-tracking to avoid duplicate processing
# - Strong verification with syntactic and structural checks
# - Error handling and retry for LLM/API failures
# - Stable termination: require consecutive verification passes before stopping early

class Action(ABC):
    """Base action class with LLM retry handling and standardized contract.

    Responsibilities:
    - Provide run(...) coroutine returning a text result.
    - Manage LLM calls with retries/backoff and robust error detection.
    """
    name: str = "Action"
    context: Optional[Context] = None
    llm: Optional[LLMInterface] = None
    max_retries: int = 3
    base_backoff: float = 1.0  # seconds

    def __init__(self, **kwargs):
        self.context = kwargs.get('context')
        try:
            if self.context and getattr(self.context, "config", None) and self.context.config.llm:
                self.llm = LLMInterface(self.context.config.llm)
        except Exception:
            self.llm = None

    async def _ask_with_retry(self, messages: List[Dict[str, str]]) -> str:
        """Call the LLM with retries and exponential backoff. Returns a string (or clear error)."""
        last_err = None
        for attempt in range(1, self.max_retries + 1):
            try:
                if self.context and self.context.tracer:
                    self.context.tracer.log("LLM_CALL", self.name, f"Attempt {attempt}/{self.max_retries}")
                if not self.llm:
                    # deterministic fallback to avoid transient dependency failure
                    fallback = "LLM_UNAVAILABLE: fallback response"
                    if self.context and self.context.tracer:
                        self.context.tracer.log("LLM_FALLBACK", self.name, fallback)
                    return fallback
                resp = await self.llm.ask(messages)
                # treat responses beginning with "Error" as failure
                if isinstance(resp, str) and resp.strip().lower().startswith("error"):
                    last_err = resp
                    raise RuntimeError(resp)
                return resp
            except Exception as e:
                last_err = str(e)
                if self.context and self.context.tracer:
                    self.context.tracer.log("LLM_ERROR", self.name, f"Attempt {attempt} failed: {last_err}")
                # backoff before next attempt
                await asyncio.sleep(self.base_backoff * (2 ** (attempt - 1)))
        # exhausted retries
        final = f"LLM_FAILED_AFTER_RETRIES: {last_err}"
        if self.context and self.context.tracer:
            self.context.tracer.log("LLM_FINAL_FAILURE", self.name, final)
        return final

    @abstractmethod
    async def run(self, *args, **kwargs) -> str:
        pass

class SimpleWriteCode(Action):
    """Produce an initial implementation from an idea."""
    name = "SimpleWriteCode"

    async def run(self, idea: str) -> str:
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, f"Idea len={len(idea or '')}")
        prompt = (
            "You are a professional Python developer. Produce a compact, production-ready Python implementation "
            "for the described task. Include docstrings, input validation, and error handling. "
            "Return only the Python source code."
            f"\n\nTask: {idea}"
        )
        messages = [
            {"role": "system", "content": "You are an expert Python programmer."},
            {"role": "user", "content": prompt}
        ]
        result = await self._ask_with_retry(messages)
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, f"Generated len={len(result)}")
        return result

class SimpleWriteTest(Action):
    """Generate pytest-style tests for a given code snippet."""
    name = "SimpleWriteTest"

    async def run(self, code: str) -> str:
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, f"Code len={len(code or '')}")
        snippet = (code or "")[:4000]
        prompt = (
            "You are a QA engineer. Given the implementation below, produce pytest tests that cover normal behavior, "
            "edge cases, and error conditions. Use clear test names and docstrings. Return only pytest code.\n\n"
            f"Implementation:\n{snippet}"
        )
        messages = [
            {"role": "system", "content": "You are an expert QA engineer."},
            {"role": "user", "content": prompt}
        ]
        result = await self._ask_with_retry(messages)
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, f"Tests len={len(result)}")
        return result

class SimpleWriteReview(Action):
    """Review code and tests and produce actionable items."""

    name = "SimpleWriteReview"

    def __init__(self, is_human: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.is_human = is_human

    async def run(self, code: str, tests: str) -> str:
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, f"Human={self.is_human}")
        # Static checks
        issues = []
        try:
            ast.parse(code or "")
        except Exception as e:
            issues.append(f"code_syntax_error: {str(e)[:160]}")
        try:
            ast.parse(tests or "")
        except Exception as e:
            issues.append(f"tests_syntax_error: {str(e)[:160]}")
        if self.is_human:
            review = "HUMAN_REVIEW: " + ("; ".join(issues) if issues else "ok")
        else:
            prompt = (
                "You are a senior engineer. Provide a concise, structured review (VERDICT: PASS/FAIL) and actionable items. "
                "Include any static issues found.\n\n"
                f"Code:\n{(code or '')[:2000]}\n\nTests:\n{(tests or '')[:2000]}\n\n"
                f"STATIC_ISSUES: {issues}"
            )
            messages = [
                {"role": "system", "content": "You are a senior software engineer doing code reviews."},
                {"role": "user", "content": prompt}
            ]
            llm_resp = await self._ask_with_retry(messages)
            # fall back to static-only if llm failed
            if isinstance(llm_resp, str) and llm_resp.startswith("LLM_FAILED_AFTER_RETRIES"):
                review = "REVIEW_FAIL: " + "; ".join(issues) if issues else "REVIEW_PASS: minimal"
            else:
                review = llm_resp
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, f"Review len={len(review)}")
        return review

class SimpleVerify(Action):
    """Perform strong verification: syntax, tests presence, assertions, and references."""
    name = "SimpleVerify"

    async def run(self, code: str, tests: str) -> str:
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, "Verifying code/tests")
        status = []
        code_ok = False
        tests_ok = False
        references_ok = False

        # Check code syntax
        if not code or not code.strip():
            status.append("code: empty")
        else:
            try:
                parsed_code = ast.parse(code)
                code_ok = True
                status.append("code_syntax: ok")
            except Exception as e:
                status.append(f"code_syntax: fail ({str(e)[:160]})")
                parsed_code = None

        # Check tests syntax and assertions
        if not tests or not tests.strip():
            status.append("tests: empty")
        else:
            try:
                parsed_tests = ast.parse(tests)
                # heuristic: look for pytest functions or assert statements
                has_test_fn = any(isinstance(n, ast.FunctionDef) and n.name.startswith("test_") for n in ast.walk(parsed_tests))
                has_assert = any(isinstance(n, ast.Assert) for n in ast.walk(parsed_tests))
                if has_test_fn or has_assert:
                    tests_ok = True
                    status.append("tests_syntax_and_asserts: ok")
                else:
                    status.append("tests_syntax: ok_but_no_tests_found")
                parsed_tests = parsed_tests
            except Exception as e:
                status.append(f"tests_syntax: fail ({str(e)[:160]})")
                parsed_tests = None

        # Check tests reference functions in code
        if code_ok and tests_ok and parsed_code and parsed_tests:
            func_names = {n.name for n in ast.walk(parsed_code) if isinstance(n, ast.FunctionDef)}
            tests_text = tests or ""
            if func_names:
                for fn in func_names:
                    if fn in tests_text:
                        references_ok = True
                        break
                if references_ok:
                    status.append("tests_reference_functions: ok")
                else:
                    status.append("tests_reference_functions: fail (no references)")
            else:
                status.append("tests_reference_functions: warn (no top-level functions in code)")

        verified = code_ok and tests_ok and references_ok
        result = f"VERIFICATION_RESULT: {'PASS' if verified else 'FAIL'} | " + "; ".join(status)
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, result)
        return result

class Role(ABC):
    """Base role with clear responsibilities and processed-tracking to avoid duplicates.

    Responsibilities:
    - Decide whether to handle a message (match send_to or watch_list)
    - Execute its single main action and produce a Message with routing metadata (send_to)
    """
    name: str = "Role"
    profile: str = "Default"
    context: Optional[Context] = None
    actions: List[Action] = []
    watch_list: List[str] = []

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.name)
        self.profile = kwargs.get('profile', self.profile)
        self.context = kwargs.get('context')
        self.is_human = kwargs.get('is_human', False)
        self.actions = []
        self.watch_list = []
        self.env: Optional["Environment"] = None
        # track processed (message ids) per role to avoid reprocessing
        self._processed_ids: Set[str] = set()

    def set_actions(self, actions: List[Action]):
        self.actions = actions

    def _watch(self, actions: List[Type[Action]]):
        # store names for robust matching
        self.watch_list = [a.name for a in actions]

    def _should_handle(self, msg: Message) -> bool:
        # never handle messages produced by self or already processed
        if getattr(msg, "sent_from", None) == self.name:
            return False
        if getattr(msg, "id", None) in self._processed_ids:
            return False
        # explicit routing
        send_to = getattr(msg, "send_to", None) or set(getattr(msg, "sent_to", None) or set())
        if send_to:
            if self.profile in send_to or self.name in send_to:
                return True
            return False
        # watch-list matching by cause_by
        if getattr(msg, "cause_by", None) in self.watch_list:
            return True
        return False

    async def act(self, message: Optional[Message] = None) -> Optional[Message]:
        if not self.actions:
            return None
        action = self.actions[0]
        # if message provided but not intended for this role, skip
        if message and not self._should_handle(message):
            return None
        if self.context and self.context.tracer:
            self.context.tracer.log("ROLE_ACT", self.name, f"Handling msg={getattr(message, 'id', 'none')} cause_by={getattr(message, 'cause_by', '')}")
        try:
            # Dispatch by action name (explicit)
            if action.name == SimpleWriteCode.name:
                idea = ""
                if message:
                    idea = getattr(message, "instruct_content", None) or (message.content or "")
                result_text = await action.run(idea)
                # route to tester primarily, and reviewer optionally
                send_to = {"SimpleTester"}
                if "ERROR" in result_text or result_text.startswith("LLM_FAILED") or result_text.startswith("LLM_UNAVAILABLE"):
                    # if generation failed, route back to coder (self) for retry later and to reviewer for context
                    send_to = {self.profile}
                response = Message(
                    content=result_text,
                    role=self.profile,
                    cause_by=action.name,
                    sent_from=self.name,
                    send_to=send_to
                )
            elif action.name == SimpleWriteTest.name:
                # expect code text in message.content, otherwise look up latest code in env
                code_text = ""
                if message and message.content:
                    code_text = message.content
                elif self.env:
                    # find most recent code message
                    for m in reversed(self.env.history):
                        if m.cause_by == SimpleWriteCode.name:
                            code_text = m.content
                            break
                result_text = await action.run(code_text)
                send_to = {"SimpleReviewer"}
                if result_text.startswith("LLM_FAILED") or result_text.startswith("ERROR"):
                    send_to = {"SimpleTester", "SimpleCoder"}
                response = Message(
                    content=result_text,
                    role=self.profile,
                    cause_by=action.name,
                    sent_from=self.name,
                    send_to=send_to
                )
            elif action.name == SimpleWriteReview.name:
                # collect latest code and tests from env
                code_text = ""
                tests_text = ""
                if self.env:
                    for m in reversed(self.env.history):
                        if m.cause_by == SimpleWriteCode.name and not code_text:
                            code_text = m.content
                        if m.cause_by == SimpleWriteTest.name and not tests_text:
                            tests_text = m.content
                        if code_text and tests_text:
                            break
                result_text = await action.run(code_text, tests_text)
                # If review indicates issues, route back to coder/tester; else route to verifier
                lowered = (result_text or "").lower()
                if "fail" in lowered or "error" in lowered or "syntax" in lowered:
                    send_to = {"SimpleCoder", "SimpleTester"}
                else:
                    send_to = {"SimpleVerifier"}
                response = Message(
                    content=result_text,
                    role=self.profile,
                    cause_by=action.name,
                    sent_from=self.name,
                    send_to=send_to
                )
            elif action.name == SimpleVerify.name:
                # collect latest code and tests
                code_text = ""
                tests_text = ""
                if self.env:
                    for m in reversed(self.env.history):
                        if m.cause_by == SimpleWriteCode.name and not code_text:
                            code_text = m.content
                        if m.cause_by == SimpleWriteTest.name and not tests_text:
                            tests_text = m.content
                        if code_text and tests_text:
                            break
                result_text = await action.run(code_text, tests_text)
                # verification is terminal but still broadcast to reviewer and coder for trace
                send_to = {"SimpleReviewer", "SimpleCoder", "SimpleTester"}
                response = Message(
                    content=result_text,
                    role=self.profile,
                    cause_by=action.name,
                    sent_from=self.name,
                    send_to=send_to
                )
            else:
                response = Message(
                    content="NO_OP",
                    role=self.profile,
                    cause_by=action.name,
                    sent_from=self.name
                )
        except Exception as e:
            err = f"ROLE_EXCEPTION: {str(e)}"
            if self.context and self.context.tracer:
                self.context.tracer.log("ROLE_EXCEPTION", self.name, err)
            response = Message(
                content=err,
                role=self.profile,
                cause_by="RoleException",
                sent_from=self.name,
                send_to={"SimpleCoder"}
            )

        # mark input message as processed for this role to avoid duplicate processing
        if message and getattr(message, "id", None):
            self._processed_ids.add(message.id)
        # also mark produced message id as processed locally to avoid reprocessing self-produced messages
        if getattr(response, "id", None):
            self._processed_ids.add(response.id)

        if self.context and self.context.tracer:
            self.context.tracer.log("ROLE_COMPLETE", self.name, f"Produced msg={response.id} send_to={getattr(response, 'send_to', set())}")
        return response

class SimpleCoder(Role):
    name = "Alice"
    profile = "SimpleCoder"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteCode(context=self.context)])

class SimpleTester(Role):
    name = "Bob"
    profile = "SimpleTester"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteTest(context=self.context)])
        self._watch([SimpleWriteCode])

class SimpleReviewer(Role):
    name = "Charlie"
    profile = "SimpleReviewer"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteReview(is_human=self.is_human, context=self.context)])
        self._watch([SimpleWriteTest, SimpleWriteCode])

class SimpleVerifier(Role):
    name = "Dana"
    profile = "SimpleVerifier"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleVerify(context=self.context)])
        self._watch([SimpleWriteTest, SimpleWriteReview, SimpleWriteCode])

class Environment:
    """Tracks roles, history and ensures idempotent processing via processed set."""
    def __init__(self, tracer: Optional[ExecutionTracer] = None):
        self.roles: List[Role] = []
        self.history: List[Message] = []
        self.tracer = tracer
        # processed pairs of (role_name, msg_id)
        self.processed: Set[Tuple[str, str]] = set()

    def add_role(self, role: Role):
        role.env = self
        self.roles.append(role)
        if self.tracer:
            self.tracer.log("ENV_ADD_ROLE", "Environment", f"Added role: {role.name} ({role.profile})")

    def publish_message(self, message: Message):
        # ensure send_to exists as set for compatibility
        if getattr(message, "send_to", None) is None:
            try:
                message.send_to = set(getattr(message, "sent_to", set()) or set())
            except Exception:
                message.send_to = set()
        self.history.append(message)
        if self.tracer:
            preview = (message.content or "")[:140].replace("\n", " ")
            self.tracer.log("ENV_MESSAGE", "Environment", f"Msg {message.id} from {message.sent_from} cause_by={message.cause_by} -> {list(message.send_to)} preview={preview}")

    def mark_processed(self, role: Role, message: Message):
        if getattr(message, "id", None):
            self.processed.add((role.name, message.id))
            if self.tracer:
                self.tracer.log("ENV_MARK_PROCESSED", "Environment", f"{role.name} processed {message.id}")

    def has_processed(self, role: Role, message: Message) -> bool:
        if not getattr(message, "id", None):
            return False
        return (role.name, message.id) in self.processed

    def get_messages_for_role(self, role: Role) -> List[Message]:
        """Return unprocessed messages relevant to the role (explicit routing or watch_list)."""
        out: List[Message] = []
        for msg in self.history:
            if getattr(msg, "id", None) is None:
                continue
            if (role.name, msg.id) in self.processed:
                continue
            if getattr(msg, "sent_from", None) == role.name:
                continue
            # explicit routing
            send_to = getattr(msg, "send_to", None) or set(getattr(msg, "sent_to", set()) or set())
            if send_to:
                if role.profile in send_to or role.name in send_to:
                    out.append(msg)
                    continue
            # watch-list
            if getattr(msg, "cause_by", None) in role.watch_list:
                out.append(msg)
        # maintain chronological order
        return out

class Team:
    """Orchestrates multi-agent collaboration with deterministic ordering, retries, and stable verification."""

    def __init__(self, context: Optional[Context] = None, log_file: Optional[str] = None):
        self.context = context or Context()
        self.tracer = ExecutionTracer(log_file)
        self.context.tracer = self.tracer
        self.env = Environment(self.tracer)
        self.investment: float = 20.0
        self.idea: str = ""
        self.log_file = log_file
        # verification stability tracking
        self.verifier_streak: int = 0
        self.required_stable_passes: int = 2

    def hire(self, roles: List[Role]):
        for role in roles:
            role.context = self.context
            role.env = self.env
            self.env.add_role(role)

    def invest(self, investment: float):
        self.investment = investment

    def run_project(self, idea: str):
        self.idea = idea
        self.tracer.log("TEAM_START", "Team", f"Starting project: {idea}")

    async def _process_role_messages(self, role: Role):
        msgs = self.env.get_messages_for_role(role)
        if not msgs:
            # allow role to act proactively (e.g., coder on initial round) if there is no directed message
            # but guard against spamming by checking recent history
            proactive_msg = None
            # coder proactive behavior is controlled from the orchestrator
            return
        for m in msgs:
            # call role
            resp = await role.act(m)
            # mark processed whether or not action succeeded to avoid infinite loops
            self.env.mark_processed(role, m)
            if resp:
                self.env.publish_message(resp)
                # if verifier produced PASS, update streak
                if isinstance(role, SimpleVerifier) and "VERIFICATION_RESULT: PASS" in (resp.content or ""):
                    self.verifier_streak += 1
                    self.tracer.log("VERIFIER_STREAK", "Team", f"streak={self.verifier_streak}")
                elif isinstance(role, SimpleVerifier):
                    # reset on non-pass
                    if self.verifier_streak > 0:
                        self.tracer.log("VERIFIER_RESET", "Team", f"resetting streak {self.verifier_streak}->0")
                    self.verifier_streak = 0

    async def run(self, n_round: int = 4):
        self.tracer.log("TEAM_RUN", "Team", f"Running up to {n_round} rounds (stable_passes={self.required_stable_passes})")
        # initial message targeted at coder
        initial_msg = Message(
            content=f"Let's work on this project: {self.idea}",
            instruct_content=self.idea,
            role="Human",
            sent_from="User",
            cause_by="UserInput",
            send_to={"SimpleCoder"}
        )
        self.env.publish_message(initial_msg)

        # deterministic order
        order = [SimpleCoder, SimpleTester, SimpleReviewer, SimpleVerifier]

        for round_num in range(n_round):
            self.tracer.log("ROUND_START", "Team", f"Round {round_num+1}/{n_round}")
            # For each role in order, process relevant messages
            for role_cls in order:
                roles = [r for r in self.env.roles if isinstance(r, role_cls)]
                for role in roles:
                    # special-case: allow proactive coder run on first round if not yet produced code
                    if isinstance(role, SimpleCoder) and round_num == 0:
                        # check if coder has processed the initial user message
                        user_msgs = [m for m in self.env.history if getattr(m, "cause_by", "") == "UserInput"]
                        need_init = False
                        for um in user_msgs:
                            if not self.env.has_processed(role, um):
                                need_init = True
                                break
                        if need_init:
                            await self._process_role_messages(role)
                            # continue to next role
                            continue
                    await self._process_role_messages(role)

            self.tracer.log("ROUND_END", "Team", f"Round {round_num+1} completed; verifier_streak={self.verifier_streak}; history_len={len(self.env.history)}")

            # termination: require 'required_stable_passes' consecutive PASS results
            if self.verifier_streak >= self.required_stable_passes:
                self.tracer.log("TEAM_EARLY_STOP", "Team", f"Verification stable for {self.verifier_streak} passes; stopping")
                break

            # If no messages were produced in this round (no progress), nudge coder proactively once per stalled round
            # Determine whether new messages were added this round by looking at history length changes is complex here;
            # simpler heuristic: if the last messages are not tests/verifier/reviewer, nudge coder.
            last_msgs = self.env.history[-4:] if len(self.env.history) >= 4 else self.env.history[:]
            if not any((m.cause_by == SimpleWriteTest.name or m.cause_by == SimpleWriteCode.name or m.cause_by == SimpleWriteReview.name) for m in last_msgs):
                # send a gentle nudge to coder to refine
                nudge = Message(
                    content=f"Please refine and re-run implementation for: {self.idea}",
                    instruct_content=self.idea,
                    role="System",
                    sent_from="Orchestrator",
                    cause_by="Nudge",
                    send_to={"SimpleCoder"}
                )
                self.env.publish_message(nudge)
                # process coder nudge immediately
                coder_roles = [r for r in self.env.roles if isinstance(r, SimpleCoder)]
                for coder in coder_roles:
                    await self._process_role_messages(coder)

        # finalization: log summary
        self.tracer.log("TEAM_END", "Team", "Project completed")
        summary = f"Project '{self.idea}' completed after {round_num+1} rounds with {len(self.env.history)} messages. verifier_streak={self.verifier_streak}"
        self.tracer.log("SUMMARY", "Team", summary)

# EVOLVE-BLOCK-END

# Fixed main execution function (not evolved)
async def run_multi_agent_task(idea: str, n_rounds: int = 4, log_file: str = None):
    """Run a multi-agent task and return the trace"""
    # Create context
    context = Context()
    context.config.llm.api_key = os.getenv("OPENAI_API_KEY", "fake-key")
    
    # Create team
    team = Team(context=context, log_file=log_file)
    team.hire([
        SimpleCoder(context=context),
        SimpleTester(context=context),
        SimpleReviewer(context=context),
        SimpleVerifier(context=context)
    ])
    
    team.invest(investment=15.0)
    team.run_project(idea)
    await team.run(n_round=n_rounds)
    
    # Return the trace content
    if log_file and os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return f.read()
    return ""