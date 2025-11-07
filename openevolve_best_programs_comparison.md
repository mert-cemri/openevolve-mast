# Comparison of Best Evolved Multi-Agent Programs

This document provides a comprehensive comparison of three evolved multi-agent systems, highlighting their architectural differences, design patterns, and evolution strategies.

## Overview

| System | Evolution Iterations | Key Focus | Final Architecture |
|--------|---------------------|-----------|-------------------|
| **metagpt_evolution_v2** | 175 | Simplicity & Robustness | Minimal, fail-safe design |
| **multi_agent_evolution_v2** | 100 | Information Flow | Defensive programming with artifact tracking |
| **multi_agent_evolution_v3_gpt5** | 200 | Advanced Error Handling | Sophisticated retry & verification |

## 1. Error Handling & LLM Interaction

### metagpt_evolution_v2: Simple Exception Swallowing
```python
async def act(self, inbound: Message) -> Optional[Message]:
    """Perform action; swallow & log all exceptions."""
    self.memory.append(inbound)
    try:
        result = await self.action.run(inbound.content)
        return Message(
            content=result,
            role=self.role_type,
            cause_by=self.action.name,
            sent_from=self.name,
        )
    except Exception as exc:
        if self.context.tracer:
            self.context.tracer.log_team_coordination("AGENT_ERROR", f"{self.name} crashed: {exc}")
        return None  # Never crash, always return None
```

### multi_agent_evolution_v2: Defensive LLM Usage
```python
def _should_use_llm(ctx: Optional[Context]) -> bool:
    if not (ctx and aiohttp):
        return False
    key = ctx.config.llm.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
    return os.getenv("ENABLE_REAL_LLM", "0") == "1" and key != "fake-key"

class Action(ABC):
    def __init__(self, *, context: Optional[Context] = None):
        self.context = context
        self.llm: Optional[LLMInterface] = (
            LLMInterface(context.config.llm) if _should_use_llm(context) else None
        )
```

### multi_agent_evolution_v3_gpt5: Sophisticated Retry with Backoff
```python
class Action(ABC):
    max_retries: int = 3
    base_backoff: float = 1.0  # seconds

    async def _ask_with_retry(self, messages: List[Dict[str, str]]) -> str:
        """Call the LLM with retries and exponential backoff."""
        last_err = None
        for attempt in range(1, self.max_retries + 1):
            try:
                if not self.llm:
                    return "LLM_UNAVAILABLE: fallback response"
                resp = await self.llm.ask(messages)
                # Intelligent error detection
                if isinstance(resp, str) and resp.strip().lower().startswith("error"):
                    last_err = resp
                    raise RuntimeError(resp)
                return resp
            except Exception as e:
                last_err = str(e)
                await asyncio.sleep(self.base_backoff * (2 ** (attempt - 1)))
        return f"LLM_FAILED_AFTER_RETRIES: {last_err}"
```

**Key Differences**:
- **v2 (MetaGPT)**: Simple try-catch, swallow all exceptions
- **v2 (Multi-Agent)**: Check LLM availability before use
- **v3 (GPT5)**: Advanced retry mechanism with exponential backoff

## 2. Agent Architecture & State Management

### metagpt_evolution_v2: Minimal Agent State
```python
class EvolvingAgent:
    def __init__(self, role_type: str, context: Context, name: str = "", **_):
        self.role_type = role_type
        self.context = context
        self.name = name or f"{role_type}_Agent"
        self.memory: List[Message] = []
        
        # Direct action mapping
        action_cls = _ROLE_TO_ACTION.get(role_type.lower(), CodeAction)
        self.action = action_cls(context)
```

### multi_agent_evolution_v2: Shared Context for Artifacts
```python
class SimpleWriteReview(Action):
    async def run(self) -> str:
        # Pull artifacts from shared context
        code = self.context.artefacts.get("code", "# No code provided")
        tests = self.context.artefacts.get("tests", "# No tests provided")
        # Review logic...
```

### multi_agent_evolution_v3_gpt5: Message Deduplication Tracking
```python
class Role(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.name)
        self.profile = kwargs.get('profile', self.profile)
        self.context = kwargs.get('context')
        # Track processed message IDs to avoid reprocessing
        self._processed_ids: Set[str] = set()
    
    def _should_act(self, message: Message) -> bool:
        """Determine if this role should act on the message"""
        if message.id in self._processed_ids:
            return False  # Already processed
        # Check explicit routing or watch list
        if message.send_to:
            return self.name in message.send_to
        return message.cause_by in self.watch_list
```

**Key Differences**:
- **v2 (MetaGPT)**: Minimal state, single action per agent
- **v2 (Multi-Agent)**: Shared context for artifact storage
- **v3 (GPT5)**: Sophisticated tracking to prevent duplicate processing

## 3. Communication & Message Routing

### metagpt_evolution_v2: Simple Sequential Flow
```python
async def execute_evolving_workflow(agents, idea, cfg, tracer) -> str:
    pattern = cfg.workflow_pattern
    if pattern == "parallel":
        replies = await asyncio.gather(*[ag.act(init_msg) for ag in agents])
        messages.extend([m for m in replies if m])
    else:  # default "waterfall"
        current = init_msg
        for ag in agents:
            reply = await ag.act(current)
            if reply:
                messages.append(reply)
                current = reply
```

### multi_agent_evolution_v2: Artifact Propagation
```python
# Explicit artifact propagation through message metadata
if isinstance(action, SimpleWriteCode):
    msg.instruct_content = output  # Embed code here
elif isinstance(action, SimpleWriteTest):
    msg.instruct_content = self.context.artefacts.get("code", "")

# Store artifacts in context
if isinstance(role, SimpleCoder):
    self.context.artefacts["code"] = result.content
```

### multi_agent_evolution_v3_gpt5: Explicit Routing with send_to
```python
class SimpleCoder(Role):
    async def act(self, message: Optional[Message]) -> Optional[Message]:
        # Generate code...
        return Message(
            content=code_result,
            role=self.profile,
            cause_by="SimpleWriteCode",
            sent_from=self.name,
            send_to={"Bob"}  # Explicitly route to tester
        )

class Environment:
    def _match_route(self, message: Message, role: Role) -> bool:
        """Check if message should be routed to role"""
        if message.send_to:
            return role.name in message.send_to
        return message.cause_by in role.watch_list
```

**Key Differences**:
- **v2 (MetaGPT)**: Simple sequential or parallel execution
- **v2 (Multi-Agent)**: Uses instruct_content for artifact passing
- **v3 (GPT5)**: Explicit routing with send_to sets

## 4. Verification & Quality Control

### metagpt_evolution_v2: No Built-in Verification
```python
# Simple execution without verification
async def run_evolving_multi_agent_system(idea, context, tracer, n_rounds=1):
    """Orchestrates the system exactly once"""
    cfg = ArchitectureConfig()
    agents = await create_evolving_team(context, cfg)
    result = await execute_evolving_workflow(agents, idea, cfg, tracer)
    return result
```

### multi_agent_evolution_v2: Basic Review Action
```python
class SimpleWriteReview(Action):
    async def run(self) -> str:
        prompt = (
            "You are a senior engineer. Review this code and tests. "
            "Provide: quality assessment, bugs, improvements, rating (1-10)."
        )
        # Basic LLM review
```

### multi_agent_evolution_v3_gpt5: Multi-Layer Verification
```python
class SimpleWriteReview(Action):
    async def run(self, code: str, tests: str) -> str:
        # Static AST checks first
        issues = []
        try:
            ast.parse(code or "")
        except Exception as e:
            issues.append(f"code_syntax_error: {str(e)[:160]}")
        try:
            ast.parse(tests or "")
        except Exception as e:
            issues.append(f"tests_syntax_error: {str(e)[:160]}")
        
        # Structured review with verdict
        prompt = (
            "Provide a structured review (VERDICT: PASS/FAIL) and actionable items. "
            f"STATIC_ISSUES: {issues}"
        )
        
        # Stable termination logic
        if "VERDICT: PASS" in review:
            self.consecutive_passes += 1
            if self.consecutive_passes >= 2:
                return "STABLE_PASS"
```

**Key Differences**:
- **v2 (MetaGPT)**: No verification logic
- **v2 (Multi-Agent)**: Simple LLM-based review
- **v3 (GPT5)**: Static analysis + structured verdicts + consecutive pass requirement

## 5. Workflow Patterns

### metagpt_evolution_v2: Fixed Patterns
```python
class ArchitectureConfig:
    def __init__(self):
        self.workflow_pattern = "waterfall"  # or "parallel", "iterative"
        
# Fixed 3 iterations for iterative pattern
if pattern == "iterative":
    for _ in range(3):
        for ag in agents:
            reply = await ag.act(current)
```

### multi_agent_evolution_v2: Role-Based Triggers
```python
for role in self.env.roles:
    if rnd == 0 and isinstance(role, SimpleCoder):
        trigger = kickoff
    else:
        msgs = self.env.messages_for(role)
        trigger = msgs[-1] if msgs else None
    
    if trigger:
        result = await role.act(trigger)
```

### multi_agent_evolution_v3_gpt5: Early Termination
```python
async def run(self, n_round: int = 3):
    consecutive_passes = 0
    for round_num in range(n_round):
        # Execute agents...
        
        # Check for stable termination
        if "VERDICT: PASS" in review_content:
            consecutive_passes += 1
            if consecutive_passes >= 2:
                self.tracer.log("EARLY_TERMINATION", 
                              f"Stable after {consecutive_passes} passes")
                break
        else:
            consecutive_passes = 0  # Reset on failure
```

**Key Differences**:
- **v2 (MetaGPT)**: Fixed workflow patterns
- **v2 (Multi-Agent)**: Role-based message triggers
- **v3 (GPT5)**: Dynamic termination based on quality

## 6. Logging & Observability

### metagpt_evolution_v2: Team Coordination Logs
```python
self.context.tracer.log_team_coordination("AGENT_ERROR", f"{self.name} crashed: {exc}")
self.context.tracer.log_team_coordination("WORKFLOW_START", cfg.workflow_pattern)
```

### multi_agent_evolution_v2: Centralized Logging Helper
```python
def _log(self, evt: str, details: str):
    if self.context and self.context.tracer:
        self.context.tracer.log(evt, self.name, details)

# Usage
self._log("ACTION_START", f"Generating code for idea: {idea[:60]}")
self._log("ACTION_END", f"Code length: {len(code)}")
```

### multi_agent_evolution_v3_gpt5: Detailed LLM Tracking
```python
self.context.tracer.log("LLM_CALL", self.name, f"Attempt {attempt}/{self.max_retries}")
self.context.tracer.log("LLM_ERROR", self.name, f"Attempt {attempt} failed: {last_err}")
self.context.tracer.log("LLM_FINAL_FAILURE", self.name, final)
self.context.tracer.log("STATIC_CHECK", self.name, f"Issues found: {issues}")
```

**Key Differences**:
- **v2 (MetaGPT)**: High-level coordination events
- **v2 (Multi-Agent)**: Action-level logging with helpers
- **v3 (GPT5)**: Detailed LLM interaction tracking

## Summary of Architectural Philosophies

### metagpt_evolution_v2: "Simplicity is Robustness"
- Minimal state and configuration
- All exceptions caught and logged
- Fixed, predictable execution patterns
- No complex verification logic

### multi_agent_evolution_v2: "Information Must Flow"
- Explicit artifact propagation
- Shared context for data storage
- Defensive programming everywhere
- Clear separation of concerns

### multi_agent_evolution_v3_gpt5: "Intelligence Through Sophistication"
- Advanced retry mechanisms
- Multi-layer verification
- Dynamic workflow adaptation
- Comprehensive error tracking

Each system represents a different evolution path:
- **MetaGPT** evolved toward radical simplicity
- **Multi-Agent v2** evolved toward reliable information flow
- **Multi-Agent v3** evolved toward intelligent error handling

The choice between them depends on requirements:
- Use **MetaGPT** style for maximum reliability
- Use **Multi-Agent v2** style for complex data flows
- Use **Multi-Agent v3** style for production systems needing sophisticated error handling