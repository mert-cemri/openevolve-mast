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

class Action(ABC):
    """Base action class with error handling and retry support."""
    name: str = "Action"
    context: Optional[Context] = None
    llm: Optional[LLMInterface] = None
    max_retries: int = 2
    
    def __init__(self, **kwargs):
        self.context = kwargs.get('context')
        self.max_retries = kwargs.get('max_retries', 2)
        if self.context and getattr(self.context, "config", None) and self.context.config.llm:
            self.llm = LLMInterface(self.context.config.llm)
    
    async def safe_ask(self, messages: List[Dict[str, str]]) -> str:
        """Ask the LLM with retry and exponential backoff. Returns result or error string."""
        attempt = 0
        last_err = None
        while attempt <= self.max_retries:
            attempt += 1
            if self.context and self.context.tracer:
                self.context.tracer.log("LLM_ASK", self.name, f"Attempt {attempt}/{self.max_retries+1}")
            try:
                if not self.llm:
                    return "LLM_UNAVAILABLE: Using fallback response."
                res = await self.llm.ask(messages)
                # treat responses starting with "Error:" or "Error communicating" as failures
                if isinstance(res, str) and (res.startswith("Error:") or res.startswith("Error communicating")):
                    last_err = res
                    if self.context and self.context.tracer:
                        self.context.tracer.log("LLM_ERROR", self.name, f"LLM returned error text: {res[:200]}")
                    # fall through to retry
                else:
                    return res
            except Exception as e:
                last_err = f"Exception: {e}"
                if self.context and self.context.tracer:
                    self.context.tracer.log("LLM_EXCEPTION", self.name, str(e))
            # simple backoff
            if attempt <= self.max_retries:
                # we don't want to import time in evolve block; just log retry
                if self.context and self.context.tracer:
                    self.context.tracer.log("LLM_RETRY", self.name, f"Retrying LLM ask (attempt {attempt + 1})")
        # all attempts failed
        return last_err or "LLM_UNKNOWN_ERROR"

    @abstractmethod
    async def run(self, *args, **kwargs):
        """Run the action"""
        raise NotImplementedError()

class SimpleWriteCode(Action):
    """Action to write code based on requirements"""
    name: str = "SimpleWriteCode"
    
    async def run(self, idea: str) -> str:
        """Generate code based on the idea, with validation and retries"""
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, f"Writing code for idea (len={len(idea or '')})")
        
        if not idea or not idea.strip():
            warning = "# WARNING: Empty idea provided. No code generated."
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_WARN", self.name, "Empty idea; returning warning code")
            return warning
        
        prompt = f"""You are a professional programmer. Write Python code for the following task:
Task: {idea}

Requirements:
1. Write clean, functional Python code
2. Include proper error handling
3. Add comments explaining the logic
4. Make it production-ready

Provide only the Python code with no surrounding backticks or explanations."""
        
        messages = [
            {"role": "system", "content": "You are an expert Python programmer."},
            {"role": "user", "content": prompt}
        ]
        
        code = await self.safe_ask(messages)
        # Basic validation: ensure non-empty and syntactically parseable (best-effort)
        import ast
        try:
            if not code or not isinstance(code, str) or code.strip() == "":
                raise ValueError("Empty code returned")
            ast.parse(code)
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_VALIDATE", self.name, "Code parsed successfully")
        except Exception as e:
            # Return explicit error result so downstream roles can detect and trigger retries
            err = f"# CODE_GENERATION_ERROR: {str(e)}\n# Raw Output:\n{(code or '')}"
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_ERROR", self.name, f"Validation failed: {e}")
            return err
        
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, f"Generated code length={len(code)}")
        return code

class SimpleWriteTest(Action):
    """Action to write tests for code"""
    name: str = "SimpleWriteTest"
    
    async def run(self, code: str) -> str:
        """Generate tests for the given code, validate presence of test functions"""
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, "Writing tests for code")
        
        if not code or not code.strip():
            msg = "# WARNING: No code to test. Generated placeholder tests."
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_WARN", self.name, "No code provided for tests")
            return msg
        
        prompt = f"""You are a QA engineer. Write comprehensive tests for the following code:

Code:
{code[:2000]}

Requirements:
1. Write pytest-style test cases
2. Cover edge cases and error conditions
3. Include both positive and negative tests
4. Add docstrings to explain what each test does

Provide only the Python test code with no surrounding backticks or explanations."""
        
        messages = [
            {"role": "system", "content": "You are an expert QA engineer."},
            {"role": "user", "content": prompt}
        ]
        
        tests = await self.safe_ask(messages)
        
        # Basic validation: ensure at least one function called test_
        import ast
        try:
            if not tests or not isinstance(tests, str) or tests.strip() == "":
                raise ValueError("Empty tests returned")
            parsed = ast.parse(tests)
            has_test = any(
                isinstance(n, ast.FunctionDef) and n.name.startswith("test_") for n in parsed.body
            )
            if not has_test:
                raise ValueError("No pytest-style test functions found (test_ prefix)")
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_VALIDATE", self.name, "Tests parsed and contain test_ functions")
        except Exception as e:
            err = f"# TEST_GENERATION_ERROR: {str(e)}\n# Raw Output:\n{(tests or '')}"
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_ERROR", self.name, f"Validation failed: {e}")
            return err
        
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, f"Generated tests length={len(tests)}")
        return tests

class SimpleWriteReview(Action):
    """Action to review code and tests"""
    name: str = "SimpleWriteReview"
    
    def __init__(self, is_human: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.is_human = is_human
    
    async def run(self, code: str, tests: str) -> str:
        """Review the code and tests and provide actionable items"""
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, f"Reviewing code/tests (human={self.is_human})")
        
        if self.is_human:
            review = "Human review: Please verify edge cases and error handling; consider input validation."
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_HUMAN_REVIEW", self.name, "Simulated human review provided")
            return review
        
        prompt = f"""You are a senior code reviewer. Review the following code and tests:

Code (first 1500 chars):
{code[:1500]}

Tests (first 1500 chars):
{tests[:1500]}

Focus on:
1. Code quality and best practices
2. Test coverage and missing edge cases
3. Potential bugs or issues
4. Concrete suggestions for improvement

Provide a concise, actionable review."""
        
        messages = [
            {"role": "system", "content": "You are a senior software engineer doing code review."},
            {"role": "user", "content": prompt}
        ]
        
        review = await self.safe_ask(messages)
        if not review or not isinstance(review, str):
            review = "REVIEW_ERROR: No review generated."
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_ERROR", self.name, "No review returned from LLM")
        else:
            if self.context and self.context.tracer:
                self.context.tracer.log("ACTION_END", self.name, f"Review generated len={len(review)}")
        return review

class SimpleVerify(Action):
    """Action to verify code and tests and decide readiness"""
    name: str = "SimpleVerify"

    async def run(self, code: str, tests: str) -> str:
        import ast
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_START", self.name, "Verifying code and tests")
        details = []
        code_ok = False
        tests_ok = False
        # Syntax checks
        try:
            if not code or not code.strip():
                raise ValueError("Empty code")
            ast.parse(code)
            code_ok = True
            details.append("code_syntax: ok")
        except Exception as e:
            details.append(f"code_syntax: fail ({str(e)[:120]})")
        try:
            if not tests or not tests.strip():
                raise ValueError("Empty tests")
            parsed_tests = ast.parse(tests)
            # heuristic: presence of at least one test_ function
            has_tests = any(isinstance(n, ast.FunctionDef) and n.name.startswith("test_") for n in parsed_tests.body)
            if has_tests:
                tests_ok = True
                details.append("tests_syntax_and_presence: ok")
            else:
                details.append("tests_syntax_and_presence: fail (no test_ functions found)")
        except Exception as e:
            details.append(f"tests_syntax: fail ({str(e)[:120]})")
        # Coverage heuristics: ensure functions in code are referenced by tests (simple name match)
        coverage_ok = False
        if code_ok and tests_ok:
            try:
                parsed_code = ast.parse(code)
                func_names = {n.name for n in parsed_code.body if isinstance(n, ast.FunctionDef)}
                # look for function names in test source
                tests_text = tests
                matched = [fn for fn in func_names if fn and fn in tests_text]
                if func_names and matched:
                    coverage_ok = True
                    details.append(f"coverage_hint: ok (matched functions: {matched[:5]})")
                else:
                    details.append("coverage_hint: fail (no clear function usage in tests)")
            except Exception as e:
                details.append(f"coverage_check_error: {str(e)[:120]}")
        verified = code_ok and tests_ok and coverage_ok
        result = f"VERIFICATION_RESULT: {'PASS' if verified else 'FAIL'} | " + "; ".join(details)
        if self.context and self.context.tracer:
            self.context.tracer.log("ACTION_END", self.name, result)
        return result

class Role(ABC):
    """Base role class for agents."""
    name: str = "Role"
    profile: str = "Default"
    context: Optional[Context] = None
    actions: List[Action] = []
    watch_list: List[Type[Action]] = []
    triggers_on: List[str] = []  # cause_by values this role listens for
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.name)
        self.profile = kwargs.get('profile', self.profile)
        self.context = kwargs.get('context')
        self.is_human = kwargs.get('is_human', False)
        self.actions = []
        self.watch_list = []
        self.triggers_on = kwargs.get('triggers_on', [])
        # reference to env may be injected by Team.hire
        self.env = None
    
    def set_actions(self, actions: List[Action]):
        """Set the actions this role can perform"""
        self.actions = actions
    
    def _watch(self, actions: List[Type[Action]]):
        """Set the actions this role watches for (by action class)"""
        self.watch_list = actions
        # also set triggers_on strings for quick matching
        self.triggers_on = [a.name for a in actions]
    
    def can_respond_to(self, msg: Message) -> bool:
        """Determine whether this role should respond to the message."""
        # If triggers_on empty, role acts proactively (e.g., coder on initial human input)
        if not self.triggers_on:
            return False
        return msg.cause_by in self.triggers_on
    
    async def act(self, message: Optional[Message] = None) -> Optional[Message]:
        """Perform the role's primary action in a guarded manner."""
        if not self.actions:
            return None
        action = self.actions[0]
        if self.context and self.context.tracer:
            self.context.tracer.log("ROLE_ACT", self.name, f"Attempting action: {action.name} on message id={(getattr(message,'id',None))}")
        try:
            # Map action type to expected inputs explicitly
            if isinstance(action, SimpleWriteCode):
                # coder expects instruction content if available, else full message content
                idea = ""
                if message:
                    idea = getattr(message, "instruct_content", None) or getattr(message, "content", "")
                result = await action.run(idea)
            elif isinstance(action, SimpleWriteTest):
                # tester expects code in message.content
                code = message.content if message else ""
                result = await action.run(code)
            elif isinstance(action, SimpleWriteReview):
                # reviewer needs both code and tests. Get most recent code/tests from env
                code_msg, tests_msg = None, None
                if self.env:
                    for msg in reversed(self.env.history):
                        if not code_msg and msg.cause_by == SimpleWriteCode.name:
                            code_msg = msg
                        if not tests_msg and msg.cause_by == SimpleWriteTest.name:
                            tests_msg = msg
                        if code_msg and tests_msg:
                            break
                code_text = code_msg.content if code_msg else ""
                tests_text = tests_msg.content if tests_msg else ""
                result = await action.run(code_text, tests_text)
            elif isinstance(action, SimpleVerify):
                # verifier obtains latest code/tests similar to reviewer
                code_msg, tests_msg = None, None
                if self.env:
                    for msg in reversed(self.env.history):
                        if not code_msg and msg.cause_by == SimpleWriteCode.name:
                            code_msg = msg
                        if not tests_msg and msg.cause_by == SimpleWriteTest.name:
                            tests_msg = msg
                        if code_msg and tests_msg:
                            break
                code_text = code_msg.content if code_msg else ""
                tests_text = tests_msg.content if tests_msg else ""
                result = await action.run(code_text, tests_text)
            else:
                result = await action.run(message) if message else await action.run()
        except Exception as e:
            # Catch any unexpected errors, create a failure message describing it
            err_text = f"ROLE_EXCEPTION: {self.name} failed with exception {str(e)}"
            if self.context and self.context.tracer:
                self.context.tracer.log("ROLE_EXCEPTION", self.name, err_text)
            result = err_text
        # Build a Message for the environment describing the result
        response = Message(
            content=result,
            role=self.profile,
            cause_by=action.name if action else "",
            sent_from=self.name
        )
        if self.context and self.context.tracer:
            self.context.tracer.log("ROLE_COMPLETE", self.name, f"Produced message caused by {response.cause_by}")
        return response

class SimpleCoder(Role):
    """Role that writes code"""
    name: str = "Alice"
    profile: str = "SimpleCoder"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteCode(context=self.context)])
        # coder listens to direct user input
        self._watch([])  # proactive; will be invoked explicitly on initial input

class SimpleTester(Role):
    """Role that writes tests"""
    name: str = "Bob"
    profile: str = "SimpleTester"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteTest(context=self.context)])
        self._watch([SimpleWriteCode])

class SimpleReviewer(Role):
    """Role that reviews code and tests"""
    name: str = "Charlie"
    profile: str = "SimpleReviewer"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteReview(is_human=self.is_human, context=self.context)])
        self._watch([SimpleWriteTest, SimpleWriteCode])

class SimpleVerifier(Role):
    """Role that verifies code and tests"""
    name: str = "Dana"
    profile: str = "SimpleVerifier"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleVerify(context=self.context)])
        self._watch([SimpleWriteTest, SimpleWriteCode])

class Environment:
    """Environment for multi-agent collaboration with explicit delivery and cursors."""
    def __init__(self, tracer: Optional[ExecutionTracer] = None):
        self.roles: List[Role] = []
        self.history: List[Message] = []
        self.tracer = tracer
        # per-role cursor to track which messages have been seen/consumed
        self.role_cursors: Dict[str, int] = {}
    
    def add_role(self, role: Role):
        """Add a role to the environment"""
        self.roles.append(role)
        # initialize cursor to 0 for this role (no messages consumed yet)
        self.role_cursors[role.name] = 0
        if self.tracer:
            self.tracer.log("ENV_ADD_ROLE", "Environment", f"Added role: {role.name} ({role.profile})")
    
    def get_roles(self, profile: Optional[str] = None) -> List[Role]:
        """Get roles by profile"""
        if profile:
            return [r for r in self.roles if r.profile == profile]
        return self.roles
    
    def publish_message(self, message: Message):
        """Publish a message to the environment"""
        self.history.append(message)
        if self.tracer:
            self.tracer.log("ENV_MESSAGE", "Environment", 
                          f"Message [{message.cause_by}] from {message.sent_from}: {message.content[:200]}")
    
    def get_pending_messages_for_role(self, role: Role) -> List[tuple]:
        """Return list of (index, Message) that the role has not yet consumed and that match its triggers."""
        results = []
        cursor = self.role_cursors.get(role.name, 0)
        for idx in range(cursor, len(self.history)):
            msg = self.history[idx]
            # role can respond if msg.cause_by matches role's triggers
            if role.triggers_on and msg.cause_by in role.triggers_on:
                results.append((idx, msg))
        return results
    
    def mark_consumed(self, role: Role, up_to_index: int):
        """Mark messages up to up_to_index (inclusive) as consumed for this role."""
        prev = self.role_cursors.get(role.name, 0)
        new_cursor = max(prev, up_to_index + 1)
        self.role_cursors[role.name] = new_cursor
        if self.tracer:
            self.tracer.log("ENV_CURSOR", "Environment", f"Role {role.name} cursor advanced to {new_cursor}")

class Team:
    """Team of agents working together with improved orchestration, termination and verification logic."""
    def __init__(self, context: Optional[Context] = None, log_file: Optional[str] = None):
        self.context = context or Context()
        self.tracer = ExecutionTracer(log_file)
        self.context.tracer = self.tracer
        self.env = Environment(self.tracer)
        self.investment: float = 20.0
        self.idea: str = ""
        self.log_file = log_file
        # order of execution for each round
        self.role_order = []
    
    def hire(self, roles: List[Role]):
        """Hire roles into the team and wire environment references"""
        for role in roles:
            role.context = self.context
            role.env = self.env
            self.env.add_role(role)
        # stable execution order: coder, tester, reviewer, verifier (by class)
        # maintain roles in the order they were added if present
        name_to_role = {r.__class__.__name__: r for r in self.env.roles}
        ordered = []
        for cname in ("SimpleCoder", "SimpleTester", "SimpleReviewer", "SimpleVerifier"):
            r = name_to_role.get(cname)
            if r:
                ordered.append(r)
        # fallback to any roles not listed
        for r in self.env.roles:
            if r not in ordered:
                ordered.append(r)
        self.role_order = ordered
    
    def invest(self, investment: float):
        """Set investment/budget"""
        self.investment = investment
    
    def run_project(self, idea: str):
        """Set the project idea"""
        self.idea = idea
        self.tracer.log("TEAM_START", "Team", f"Starting project: {idea}")
    
    async def run(self, n_round: int = 4):
        """Run the team collaboration for n rounds with robust termination rules."""
        self.tracer.log("TEAM_RUN", "Team", f"Running up to {n_round} rounds")
        
        # Initial message with the idea
        initial_msg = Message(
            content=f"Let's work on this project: {self.idea}",
            instruct_content=self.idea,
            role="Human",
            sent_from="User",
            cause_by="UserInput"
        )
        self.env.publish_message(initial_msg)
        
        verified = False
        last_verification_index = -1
        stable_verification_rounds = 0
        max_stable_rounds_required = 1  # require verification to remain true across a round to stop
        
        for round_num in range(n_round):
            self.tracer.log("ROUND_START", "Team", f"Round {round_num + 1}/{n_round}")
            round_actions = []
            # Special handling: on first round, explicitly invoke coder with the initial message
            for role in self.role_order:
                # For proactive coder (listens to user input), feed initial_msg on first round
                if isinstance(role, SimpleCoder) and round_num == 0:
                    if self.tracer:
                        self.tracer.log("ORCH", "Team", f"Invoking coder {role.name} with initial idea")
                    response = await role.act(initial_msg)
                    if response:
                        self.env.publish_message(response)
                        round_actions.append((role, response))
                        # mark that coder has consumed initial input
                        self.env.mark_consumed(role, len(self.env.history)-1)
                    continue
                # For other roles and later rounds, gather pending messages
                pending = self.env.get_pending_messages_for_role(role)
                if not pending:
                    if self.tracer:
                        self.tracer.log("ORCH", "Team", f"No pending messages for {role.name}")
                    continue
                # Process each pending message in order
                for idx, msg in pending:
                    if self.tracer:
                        self.tracer.log("ORCH", "Team", f"{role.name} responding to message idx={idx} cause_by={msg.cause_by}")
                    response = await role.act(msg)
                    # Mark consumed up to this message for this role
                    self.env.mark_consumed(role, idx)
                    if response:
                        self.env.publish_message(response)
                        round_actions.append((role, response))
                        # If verifier produced a pass, capture it
                        if isinstance(role, SimpleVerifier) and isinstance(response.content, str) and "VERIFICATION_RESULT: PASS" in response.content:
                            verified = True
                            last_verification_index = len(self.env.history) - 1
            # Post-round analysis: determine termination criteria
            # If verification happened this round and is still the most recent verification result, count as stable
            if verified:
                # ensure that no new code/test messages after verification (to ensure stability)
                newest_code_or_test_idx = -1
                for i, msg in enumerate(self.env.history):
                    if msg.cause_by in (SimpleWriteCode.name, SimpleWriteTest.name):
                        newest_code_or_test_idx = max(newest_code_or_test_idx, i)
                if newest_code_or_test_idx <= last_verification_index:
                    stable_verification_rounds += 1
                else:
                    stable_verification_rounds = 0
                    # If new code/tests appeared after verification, require re-verification
                    verified = False
                self.tracer.log("VER_STATUS", "Team", f"verified={verified} stable_rounds={stable_verification_rounds}")
            else:
                stable_verification_rounds = 0
            self.tracer.log("ROUND_END", "Team", f"Round {round_num + 1} completed with {len(round_actions)} actions")
            # Terminate if verification stable for required number of rounds
            if verified and stable_verification_rounds > max_stable_rounds_required:
                self.tracer.log("TEAM_EARLY_STOP", "Team", "Verification stable; stopping early")
                break
        self.tracer.log("TEAM_END", "Team", "Project completed")
        
        # Final summary
        summary = f"Project '{self.idea}' completed after {round_num + 1} rounds with {len(self.env.history)} messages exchanged. Verified={verified}"
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