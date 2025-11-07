# OpenEvolve Changes Analysis: multi_agent_evolution_v2

## Overview
This analysis examines how OpenEvolve evolved a simpler multi-agent system over 100 iterations, focusing on practical improvements to reduce MAST failure modes.

## Initial State (iteration 0)

### Basic Architecture
```python
class Action(ABC):
    """Base action class"""
    name: str = "Action"
    context: Optional[Context] = None
    llm: Optional[LLMInterface] = None
    
    def __init__(self, **kwargs):
        self.context = kwargs.get('context')
        if self.context and self.context.config.llm:
            self.llm = LLMInterface(self.context.config.llm)
```

### Simple Actions with Basic Prompts
```python
class SimpleWriteCode(Action):
    async def run(self, idea: str) -> str:
        prompt = f"""You are a professional programmer. Write Python code for the following task:
Task: {idea}

Requirements:
1. Write clean, functional Python code
2. Include proper error handling
3. Add comments explaining the logic
4. Make it production-ready

Please provide only the code without any explanation."""
```

### Basic Role Structure
```python
class Role(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.name)
        self.profile = kwargs.get('profile', self.profile)
        self.context = kwargs.get('context')
        self.is_human = kwargs.get('is_human', False)
        self.actions = []
        self.watch_list = []
```

## Evolution at Checkpoint 50

### Major Improvements:

1. **Defensive LLM Usage**:
```python
def _should_use_llm(ctx: Optional[Context]) -> bool:
    if not (ctx and aiohttp):
        return False
    key = ctx.config.llm.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
    return os.getenv("ENABLE_REAL_LLM", "0") == "1" and key != "fake-key"
```

2. **Explicit Artifact Propagation**:
```python
"""
Explicit artefact propagation:
    • Coder → Tester  : code embedded in *instruct_content*
    • Tester → Reviewer: tests in content, code in *instruct_content*
This guarantees the reviewer always receives both code & tests.
"""
```

3. **Simplified, Focused Prompts**:
```python
async def run(self, idea: str) -> str:
    prompt = (
        "You are an expert Python developer.\n"
        f"Write production-ready Python code for the following task:\n{idea}\n"
        "Return ONLY code."
    )
```

4. **Robust Error Handling**:
```python
async def run(self, idea: str) -> str:
    self._log("ACTION_START", f"Generating code for idea: {idea[:60]}")
    if not idea:
        return "# No idea provided – nothing generated.\n"
```

5. **Centralized Logging Helper**:
```python
def _log(self, evt: str, details: str):
    if self.context and self.context.tracer:
        self.context.tracer.log(evt, self.name, details)
```

## Final Evolution at Checkpoint 100

### Key Architectural Changes:

1. **Shared Context for Artifact Storage**:
```python
class SimpleWriteReview(Action):
    async def run(self) -> str:
        # Simplified: just get artefacts from shared context
        code = self.context.artefacts.get("code", "# No code provided")
        tests = self.context.artefacts.get("tests", "# No tests provided")
```

2. **Message-Based Artifact Passing**:
```python
# Propagate artefacts through message metadata
if isinstance(action, SimpleWriteCode):
    msg.instruct_content = output  # <-- embed code here
elif isinstance(action, SimpleWriteTest):
    msg.instruct_content = self.context.artefacts.get("code", "")
```

3. **Streamlined Role Actions**:
```python
async def act(self, trigger: Optional[Message]) -> Optional[Message]:
    if not self.actions:
        return None
    action = self.actions[0]
    
    if isinstance(action, SimpleWriteCode):
        idea = (trigger.instruct_content or trigger.content) if trigger else ""
        output = await action.run(idea)
    elif isinstance(action, SimpleWriteTest):
        output = await action.run(trigger.content if trigger else "")
    elif isinstance(action, SimpleWriteReview):
        # Pull artefacts from shared context for simplicity.
        output = await action.run()
```

4. **Defensive Team Orchestration**:
```python
async def run(self, n_round: int = 3):
    for rnd in range(n_round):
        self.tracer.log("ROUND", "Team", f"Round {rnd + 1}/{n_round}")
        for role in self.env.roles:
            if rnd == 0 and isinstance(role, SimpleCoder):
                trigger = kickoff
            else:
                msgs = self.env.messages_for(role)
                trigger = msgs[-1] if msgs else None
            
            if trigger:
                result = await role.act(trigger)
                if result:
                    self.env.publish(result)
```

## Key Evolution Patterns

### 1. **Information Flow Improvements**
- Initial: Vague message passing, potential loss of context
- Evolved: Explicit artifact propagation through `instruct_content`
- Final: Shared context + message metadata ensures all agents get needed info

### 2. **Prompt Engineering**
- Initial: Verbose prompts with many requirements
- Evolved: Concise, focused prompts ("Return ONLY code")
- Result: More predictable LLM outputs

### 3. **Error Handling Evolution**
- Initial: Basic try-catch blocks
- Evolved: Guards for missing inputs at every level
- Final: Defensive programming with fallbacks everywhere

### 4. **Simplified Control Flow**
- Initial: Complex role watching and message routing
- Evolved: Direct type checking for action dispatch
- Final: Linear, predictable execution flow

### 5. **Logging and Debugging**
- Initial: Scattered logging calls
- Evolved: Centralized `_log()` helper methods
- Final: Comprehensive tracing without cluttering logic

## Summary of Key Discoveries

OpenEvolve discovered that reducing multi-agent failure modes requires:

1. **Explicit Information Flow**: Use dedicated fields (`instruct_content`) for passing artifacts
2. **Defensive Programming**: Check for None/empty at every step
3. **Simplified Prompts**: Short, direct instructions reduce LLM confusion
4. **Shared Context**: Central storage prevents information loss
5. **Type-Based Dispatch**: Direct `isinstance()` checks are clearer than abstract patterns
6. **Bounded Execution**: Fixed rounds prevent infinite loops
7. **Optional LLM**: System works with stubs when LLM unavailable

The evolution shows a clear trend from complex, abstract designs to simple, concrete implementations that are easier to debug and less prone to failure.