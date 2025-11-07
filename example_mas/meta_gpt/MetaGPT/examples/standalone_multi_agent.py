"""
Standalone Multi-Agent Example - No External MetaGPT Dependencies
This file contains a complete, self-contained implementation of a multi-agent system
inspired by MetaGPT's build_customized_multi_agents.py example.

Requirements:
    pip install aiohttp pydantic fire

Usage:
    python standalone_multi_agent.py
    python standalone_multi_agent.py --idea "create a sorting algorithm" --n_round 3
"""

import asyncio
import logging
import os
import re
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Type

try:
    import aiohttp
except ImportError:
    print("Please install aiohttp: pip install aiohttp")
    exit(1)

try:
    import fire
except ImportError:
    print("Please install fire: pip install fire")
    exit(1)

try:
    from pydantic import BaseModel, Field
except ImportError:
    print("Please install pydantic: pip install pydantic")
    exit(1)


# ============== Logging Setup ==============
class ExecutionTracer:
    """Comprehensive execution tracer for multi-agent interactions"""
    
    def __init__(self, log_file: Optional[str] = None):
        self.log_file = log_file
        self.trace_id = 0
        
    def get_next_trace_id(self) -> str:
        """Generate sequential trace ID"""
        self.trace_id += 1
        return f"T{self.trace_id:03d}"
    
    def log_agent_action_start(self, agent_name: str, action_name: str, context: str = ""):
        """Log when an agent starts an action"""
        trace_id = self.get_next_trace_id()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        message = f"""
╔══ {trace_id} ═══════════════════════════════════════════
║ AGENT ACTION START [{timestamp}]
║ Agent: {agent_name}
║ Action: {action_name}
║ Context Length: {len(context)} chars
║ Context Preview: {context[:200]}{"..." if len(context) > 200 else ""}
╚════════════════════════════════════════════════════════
"""
        self._write_log(message)
        return trace_id
    
    def log_llm_interaction(self, trace_id: str, agent_name: str, prompt: str, response: str):
        """Log LLM interaction"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        message = f"""
┌── {trace_id} LLM INTERACTION [{timestamp}] ──────────────
│ Agent: {agent_name}
│ Prompt Length: {len(prompt)} chars
│ Response Length: {len(response)} chars
│ 
│ PROMPT:
│ {prompt[:500]}{"..." if len(prompt) > 500 else ""}
│ 
│ RESPONSE:
│ {response[:500]}{"..." if len(response) > 500 else ""}
└─────────────────────────────────────────────────────────
"""
        self._write_log(message)
    
    def log_message_creation(self, trace_id: str, message: "Message"):
        """Log message creation"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        message_log = f"""
┌── {trace_id} MESSAGE CREATED [{timestamp}] ───────────────
│ Message ID: {message.id}
│ Sender: {message.sent_from or message.role}
│ Action: {message.cause_by}
│ Content Length: {len(message.content)} chars
│ Content: {message.content[:300]}{"..." if len(message.content) > 300 else ""}
└─────────────────────────────────────────────────────────
"""
        self._write_log(message_log)
    
    def log_environment_publish(self, message: "Message", watching_agents: List[str], artifacts_stored: List[str]):
        """Log environment message publishing"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        env_log = f"""
╔══ ENVIRONMENT PUBLISH [{timestamp}] ══════════════════════
║ Message ID: {message.id}
║ From: {message.sent_from or message.role}
║ Action: {message.cause_by}
║ 
║ DELIVERY STATUS:
║ • Watching Agents: {', '.join(watching_agents) if watching_agents else 'None'}
║ • Artifacts Stored: {', '.join(artifacts_stored) if artifacts_stored else 'None'}
║ 
║ ENVIRONMENT STATE:
║ • Total Messages in History: {len(artifacts_stored) + 1}
║ • Message Content: {message.content[:200]}{"..." if len(message.content) > 200 else ""}
╚══════════════════════════════════════════════════════════
"""
        self._write_log(env_log)
    
    def log_agent_observation(self, agent_name: str, observed_messages: List["Message"]):
        """Log agent observation of messages"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        obs_log = f"""
┌── AGENT OBSERVATION [{timestamp}] ───────────────────────
│ Observer: {agent_name}
│ Messages Observed: {len(observed_messages)}
│ 
│ OBSERVED MESSAGES:
"""
        for i, msg in enumerate(observed_messages):
            obs_log += f"│ {i+1}. From {msg.sent_from or msg.role} | Action: {msg.cause_by} | Length: {len(msg.content)}\n"
        
        obs_log += "└─────────────────────────────────────────────────────────\n"
        self._write_log(obs_log)
    
    def log_round_summary(self, round_num: int, total_rounds: int, messages_this_round: int):
        """Log round summary"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        summary = f"""
╔══ ROUND {round_num}/{total_rounds} SUMMARY [{timestamp}] ═══════════════════
║ Messages Exchanged This Round: {messages_this_round}
║ Round Status: {'COMPLETED' if round_num <= total_rounds else 'IN_PROGRESS'}
╚══════════════════════════════════════════════════════════
"""
        self._write_log(summary)
    
    def log_final_artifacts(self, artifacts: Dict[str, str]):
        """Log final artifacts summary"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        final_log = f"""
╔══ FINAL EXECUTION SUMMARY [{timestamp}] ═══════════════════
║ ARTIFACTS GENERATED:
"""
        for artifact_type, content in artifacts.items():
            final_log += f"║ • {artifact_type}: {len(content)} chars\n"
        
        final_log += "║\n║ DETAILED ARTIFACTS:\n"
        
        for artifact_type, content in artifacts.items():
            final_log += f"""║ 
║ ═══ {artifact_type.upper()} ═══
║ {content}
║ 
"""
        
        final_log += "╚══════════════════════════════════════════════════════════\n"
        self._write_log(final_log)
    
    def _write_log(self, message: str):
        """Write to log file and console"""
        print(message)  # Always print to console for immediate feedback
        
        if self.log_file:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(message + "\n")
            except Exception as e:
                print(f"ERROR: Failed to write to log file: {e}")

def setup_logger():
    """Setup a simple logger similar to MetaGPT's logger"""
    logger = logging.getLogger("standalone_multi_agent")
    logger.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()


# ============== Configuration Classes ==============
class LLMType(str, Enum):
    """Supported LLM types"""
    OPENAI = "openai"
    QWEN = "qwen"
    CODELLAMA = "codellama"


class LLMConfig(BaseModel):
    """Configuration for LLM providers"""
    api_type: LLMType = LLMType.OPENAI
    api_key: str = "sk-"
    base_url: str = "https://api.openai.com/v1"
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_token: int = 2048
    proxy: str = ""
    
    class Config:
        arbitrary_types_allowed = True


class Config(BaseModel):
    """Main configuration container"""
    llm: LLMConfig = Field(default_factory=LLMConfig)


class Context(BaseModel):
    """Context object that holds configuration and shared state"""
    config: Config = Field(default_factory=Config)
    cost_manager: Optional[Any] = None
    tracer: Optional[Any] = None  # Add tracer field to Context
    
    class Config:
        arbitrary_types_allowed = True


# ============== Schema Classes ==============
class Message(BaseModel):
    """Message schema for agent communication"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    content: str
    role: str = "user"
    cause_by: str = ""
    sent_from: str = ""
    send_to: Set[str] = Field(default_factory=set)
    created_at: datetime = Field(default_factory=datetime.now)
    
    def __str__(self):
        return f"{self.role}: {self.content}"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "content": self.content,
            "role": self.role,
            "cause_by": self.cause_by,
            "sent_from": self.sent_from,
            "send_to": list(self.send_to),
            "created_at": self.created_at.isoformat()
        }
    
    def get_trace_info(self) -> str:
        """Get formatted trace information for logging"""
        timestamp = self.created_at.strftime("%H:%M:%S.%f")[:-3]
        sender = self.sent_from or self.role
        receivers = ", ".join(self.send_to) if self.send_to else "Environment"
        return f"[{timestamp}] {sender} → {receivers} | Action: {self.cause_by}"


class MessageQueue:
    """Simple message queue implementation"""
    def __init__(self):
        self._queue = asyncio.Queue()
    
    async def push(self, msg: Message):
        await self._queue.put(msg)
    
    async def pop(self) -> Optional[Message]:
        try:
            return await asyncio.wait_for(self._queue.get(), timeout=0.1)
        except asyncio.TimeoutError:
            return None
    
    def empty(self) -> bool:
        return self._queue.empty()


# ============== LLM Provider ==============
class BaseLLM(ABC):
    """Base class for LLM providers"""
    def __init__(self, config: LLMConfig):
        self.config = config
    
    @abstractmethod
    async def aask(self, prompt: str) -> str:
        """Send prompt to LLM and get response"""
        pass


class SimpleLLM(BaseLLM):
    """Simple LLM implementation using OpenAI-compatible API"""
    
    async def aask(self, prompt: str) -> str:
        """Send prompt to LLM and get response"""
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.config.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_token
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.config.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                    proxy=self.config.proxy if self.config.proxy else None
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result["choices"][0]["message"]["content"]
                    else:
                        error_text = await response.text()
                        logger.error(f"LLM API error: {response.status} - {error_text}")
                        return f"Error: {response.status}"
        except Exception as e:
            logger.error(f"LLM request failed: {e}")
            return f"Error: {str(e)}"


# ============== Memory System ==============
class Memory:
    """Simple memory system for storing messages"""
    def __init__(self):
        self.storage: List[Message] = []
    
    def add(self, message: Message):
        """Add a message to memory"""
        self.storage.append(message)
    
    def get_by_role(self, role: str) -> List[Message]:
        """Get messages by role"""
        return [msg for msg in self.storage if msg.role == role]
    
    def get_by_action(self, action: str) -> List[Message]:
        """Get messages by action"""
        return [msg for msg in self.storage if msg.cause_by == action]
    
    def get(self, k: int = 0) -> List[Message]:
        """Get last k messages, or all if k=0"""
        if k <= 0:
            return self.storage
        return self.storage[-k:]
    
    def clear(self):
        """Clear all messages"""
        self.storage.clear()


# ============== Action System ==============
class Action(BaseModel):
    """Base Action class with LLM integration"""
    name: str = "Action"
    context: Optional[Context] = None
    llm: Optional[BaseLLM] = None
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.context and not self.llm:
            self.llm = SimpleLLM(self.context.config.llm)
    
    async def _aask(self, prompt: str) -> str:
        """Ask LLM a question"""
        if not self.llm:
            raise ValueError("No LLM configured for this action")
        
        response = await self.llm.aask(prompt)
        
        # Log LLM interaction if tracer is available
        if self.context and hasattr(self.context, 'tracer') and self.context.tracer:
            # Find current trace ID from the call stack (simplified approach)
            trace_id = f"T{self.context.tracer.trace_id:03d}"
            self.context.tracer.log_llm_interaction(
                trace_id, getattr(self, 'name', 'Unknown'), prompt, response
            )
        
        return response
    
    @abstractmethod
    async def run(self, *args, **kwargs):
        """Execute the action"""
        pass


class UserRequirement(Action):
    """Special action for user requirements"""
    name: str = "UserRequirement"
    
    async def run(self, requirement: str) -> str:
        return requirement


# ============== Role System ==============
class RoleReactMode(str, Enum):
    """Role reaction modes"""
    REACT = "react"
    BY_ORDER = "by_order"
    PLAN_AND_ACT = "plan_and_act"


class RoleContext(BaseModel):
    """Runtime context for a role"""
    env: Optional[Any] = None
    memory: Memory = Field(default_factory=Memory)
    state: int = 0
    todo: Optional[Action] = None
    watch: Set[str] = Field(default_factory=set)
    news: List[Message] = Field(default_factory=list)
    
    class Config:
        arbitrary_types_allowed = True


class Role(BaseModel):
    """Base Role class representing an agent"""
    name: str = "Role"
    profile: str = "Role"
    goal: str = ""
    constraints: str = ""
    desc: str = ""
    is_human: bool = False
    
    context: Optional[Context] = None
    llm: Optional[BaseLLM] = None
    actions: List[Type[Action]] = Field(default_factory=list)
    rc: RoleContext = Field(default_factory=RoleContext)
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.context and not self.llm:
            self.llm = SimpleLLM(self.context.config.llm)
        self._init_actions()
    
    def _init_actions(self):
        """Initialize action instances"""
        self.actions = [action_cls(context=self.context) for action_cls in self.actions]
    
    def set_actions(self, actions: List[Type[Action]]):
        """Set actions for the role"""
        self.actions = actions
        self._init_actions()
    
    def _watch(self, actions: List[Type[Action]]):
        """Watch for specific action outputs"""
        self.rc.watch = {action.__name__ for action in actions}
    
    async def _observe(self) -> int:
        """Observe messages from watched actions"""
        # News is already populated by the environment's publish_message
        # when it delivers messages to watching roles
        news_count = len(self.rc.news)
        
        # Log observation if there are messages
        if news_count > 0 and self.rc.env and self.rc.env.tracer:
            self.rc.env.tracer.log_agent_observation(self.name, self.rc.news)
        
        # Add news to memory for context
        for msg in self.rc.news:
            self.rc.memory.add(msg)
        
        # Clear news after processing
        processed_news = self.rc.news.copy()
        self.rc.news = []
        
        return news_count
    
    async def _think(self) -> Optional[Action]:
        """Decide what action to take"""
        if len(self.actions) == 1:
            return self.actions[0]
        
        # Simple strategy: execute actions in order
        if self.rc.state < len(self.actions):
            return self.actions[self.rc.state]
        
        return None
    
    async def _act(self) -> Message:
        """Execute the selected action"""
        # Get context from memory
        context = self.get_memories()
        
        # Start tracing
        trace_id = None
        if self.rc.env and self.rc.env.tracer:
            trace_id = self.rc.env.tracer.log_agent_action_start(
                self.name, self.rc.todo.name, context
            )
        
        # Execute action
        if hasattr(self.rc.todo, 'run'):
            if self.rc.todo.name == "SimpleWriteTest":
                result = await self.rc.todo.run(context, k=5)
            elif self.rc.todo.name in ["SimpleWriteCode", "SimpleWriteReview"]:
                result = await self.rc.todo.run(context)
            else:
                result = await self.rc.todo.run()
        else:
            result = "No run method found"
        
        # Create message
        msg = Message(
            content=result,
            role=self.profile,
            cause_by=type(self.rc.todo).__name__,
            sent_from=self.name
        )
        
        # Log message creation
        if trace_id and self.rc.env and self.rc.env.tracer:
            self.rc.env.tracer.log_message_creation(trace_id, msg)
        
        # Store in memory
        self.rc.memory.add(msg)
        
        return msg
    
    async def _react(self) -> Message:
        """React to observations"""
        # Observe environment
        await self._observe()
        
        # Think about what to do
        self.rc.todo = await self._think()
        if not self.rc.todo:
            return Message(content="No action to take", role=self.profile)
        
        # Act
        msg = await self._act()
        
        # Update state
        self.rc.state += 1
        
        return msg
    
    async def run(self, message: Optional[Message] = None) -> Message:
        """Main entry point for role execution"""
        if message:
            self.rc.memory.add(message)
        
        if self.is_human:
            # Human interaction
            response = input(f"{self.name} (human): Please provide your input: ")
            return Message(content=response, role=self.profile, sent_from=self.name)
        
        return await self._react()
    
    def get_memories(self, k: int = 0) -> str:
        """Get memory as formatted string"""
        memories = self.rc.memory.get(k)
        if not memories:
            return ""
        
        return "\n".join([f"{msg.role}: {msg.content}" for msg in memories])


# ============== Environment ==============
class Environment:
    """Environment for agent communication and shared state"""
    def __init__(self, tracer: Optional[ExecutionTracer] = None):
        self.roles: Dict[str, Role] = {}
        self.message_queue = MessageQueue()
        self.history: List[Message] = []
        self.shared_memory: Dict[str, Any] = {}  # Store artifacts like code
        self.tracer = tracer
    
    def add_role(self, role: Role):
        """Add a role to the environment"""
        self.roles[role.name] = role
        role.rc.env = self
        if self.tracer:
            self.tracer._write_log(f"ENVIRONMENT: Added role '{role.name}' ({role.profile})")
    
    async def publish_message(self, message: Message):
        """Publish a message to the environment for all roles to see"""
        self.history.append(message)
        
        # Track which agents are watching and what artifacts get stored
        watching_agents = []
        artifacts_stored = []
        
        # Store code artifacts separately for easy access
        if "SimpleWriteCode" in message.cause_by:
            self.shared_memory["latest_code"] = message.content
            artifacts_stored.append("latest_code")
        elif "SimpleWriteTest" in message.cause_by:
            self.shared_memory["latest_tests"] = message.content
            artifacts_stored.append("latest_tests")
        elif "SimpleWriteReview" in message.cause_by:
            self.shared_memory["latest_review"] = message.content
            artifacts_stored.append("latest_review")
        
        # Make message available to all watching roles
        for role_name, role in self.roles.items():
            if message.cause_by in role.rc.watch:
                role.rc.news.append(message)
                watching_agents.append(role_name)
                message.send_to.add(role_name)  # Update message with actual recipients
        
        # Log the environment publish event
        if self.tracer:
            self.tracer.log_environment_publish(message, watching_agents, artifacts_stored)
    
    def get_roles(self) -> Dict[str, Role]:
        """Get all roles in the environment"""
        return self.roles
    
    def get_artifact(self, key: str) -> Optional[str]:
        """Get a stored artifact from shared memory"""
        return self.shared_memory.get(key)
    
    def get_full_history(self) -> List[Message]:
        """Get complete message history"""
        return self.history


# ============== Team ==============
class Team:
    """Team of agents working together"""
    def __init__(self, context: Optional[Context] = None, log_file: Optional[str] = None):
        self.context = context or Context()
        self.tracer = ExecutionTracer(log_file)
        self.context.tracer = self.tracer  # Add tracer to context for actions
        self.env = Environment(self.tracer)
        self.investment: float = 10.0
        self.idea: str = ""
        self.log_file = log_file
    
    def hire(self, roles: List[Role]):
        """Hire roles into the team"""
        for role in roles:
            role.context = self.context
            self.env.add_role(role)
    
    def invest(self, investment: float):
        """Set investment/budget"""
        self.investment = investment
    
    def run_project(self, idea: str):
        """Set the project idea"""
        self.idea = idea
    
    async def run(self, n_round: int = 3):
        """Run the team for n rounds"""
        # Log initial setup
        self.tracer._write_log(f"""
╔══ MULTI-AGENT SYSTEM EXECUTION START ════════════════════
║ Project Idea: {self.idea}
║ Investment: ${self.investment}
║ Planned Rounds: {n_round}
║ Agents: {', '.join([role.name for role in self.env.get_roles().values()])}
╚═══════════════════════════════════════════════════════════
""")
        
        # Initial message
        msg = Message(
            content=self.idea,
            role="Human",
            cause_by=UserRequirement.__name__,
            sent_from="Human"
        )
        await self.env.publish_message(msg)
        
        # Run rounds
        round_message_count = 0
        for i in range(n_round):
            self.tracer.log_round_summary(i+1, n_round, 0)  # Start of round
            round_start_messages = len(self.env.history)
            
            # Run each role in sequence
            for role in self.env.get_roles().values():
                response = await role.run()
                await self.env.publish_message(response)
                round_message_count += 1
            
            # Log round completion
            round_end_messages = len(self.env.history)
            messages_this_round = round_end_messages - round_start_messages
            self.tracer.log_round_summary(i+1, n_round, messages_this_round)
        
        # Log final artifacts
        artifacts = {}
        if self.env.get_artifact("latest_code"):
            artifacts["latest_code"] = self.env.get_artifact("latest_code")
        if self.env.get_artifact("latest_tests"):
            artifacts["latest_tests"] = self.env.get_artifact("latest_tests")
        if self.env.get_artifact("latest_review"):
            artifacts["latest_review"] = self.env.get_artifact("latest_review")
        
        self.tracer.log_final_artifacts(artifacts)
        
        self.tracer._write_log(f"""
╔══ EXECUTION COMPLETE ═════════════════════════════════════
║ Total Rounds: {n_round}
║ Total Messages: {len(self.env.history)}
║ Total Artifacts: {len(artifacts)}
║ Execution Status: SUCCESS
╚═══════════════════════════════════════════════════════════
""")
    


# ============== Example Implementation ==============
def parse_code(rsp):
    """Extract code from LLM response"""
    pattern = r"```python(.*)```"
    match = re.search(pattern, rsp, re.DOTALL)
    code_text = match.group(1) if match else rsp
    return code_text


class SimpleWriteCode(Action):
    """Action to write code based on requirements"""
    PROMPT_TEMPLATE: str = """
    Write a python function that can {instruction}.
    Return ```python your_code_here ``` with NO other texts,
    your code:
    """
    name: str = "SimpleWriteCode"
    
    async def run(self, instruction: str):
        prompt = self.PROMPT_TEMPLATE.format(instruction=instruction)
        rsp = await self._aask(prompt)
        code_text = parse_code(rsp)
        return code_text


class SimpleCoder(Role):
    """Role that writes code"""
    name: str = "Alice"
    profile: str = "SimpleCoder"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch([UserRequirement])
        self.set_actions([SimpleWriteCode])


class SimpleWriteTest(Action):
    """Action to write tests for code"""
    PROMPT_TEMPLATE: str = """
    Context: {context}
    Write {k} unit tests using pytest for the given function, assuming you have imported it.
    Return ```python your_code_here ``` with NO other texts,
    your code:
    """
    name: str = "SimpleWriteTest"
    
    async def run(self, context: str, k: int = 3):
        prompt = self.PROMPT_TEMPLATE.format(context=context, k=k)
        rsp = await self._aask(prompt)
        code_text = parse_code(rsp)
        return code_text


class SimpleTester(Role):
    """Role that writes tests"""
    name: str = "Bob"
    profile: str = "SimpleTester"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteTest])
        self._watch([SimpleWriteCode, SimpleWriteReview])
    
    async def _act(self) -> Message:
        """Custom act method with logging"""
        logger.info(f"{self.profile}: executing {self.rc.todo.name}")
        todo = self.rc.todo
        
        # Collect context
        context = self.get_memories()
        
        # Perform action and get result
        code_text = await todo.run(context, k=5)
        msg = Message(content=code_text, role=self.profile, cause_by=type(todo).__name__)
        
        # Optional: Could save trace to file here if needed
        # trace = {
        #     "role": self.profile,
        #     "action": type(todo).__name__,
        #     "context": context,
        #     "output": code_text,
        # }
        
        return msg


class SimpleWriteReview(Action):
    """Action to review test cases"""
    PROMPT_TEMPLATE: str = """
    Context: {context}
    Review the test cases and provide one critical comments:
    """
    name: str = "SimpleWriteReview"
    
    async def run(self, context: str):
        prompt = self.PROMPT_TEMPLATE.format(context=context)
        rsp = await self._aask(prompt)
        return rsp


class SimpleReviewer(Role):
    """Role that reviews code and tests"""
    name: str = "Charlie"
    profile: str = "SimpleReviewer"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteReview])
        self._watch([SimpleWriteTest])


# ============== Main Function ==============
async def main(
    idea: str = "write a function that calculates the product of a list",
    investment: float = 3.0,
    n_round: int = 5,
    add_human: bool = False,
    log_file: str = None,  # If None, will auto-generate based on idea and timestamp
    model_type: str = "openai",
):
    """Main function to run the multi-agent system"""
    # Configure logging
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format)
    logger = logging.getLogger("standalone_multi_agent")
    
    # Initialize variables for later reference
    summary_file = None
    idea_log_dir = None
    
    # Create categorical log directory structure
    base_log_dir = os.path.join(os.getcwd(), "metagpt_logs")
    model_log_dir = os.path.join(base_log_dir, model_type.lower())
    
    # Create a sanitized version of the idea for directory naming
    safe_idea = re.sub(r'[^a-zA-Z0-9_-]', '_', idea[:50])  # Limit to 50 chars
    safe_idea = re.sub(r'_+', '_', safe_idea).strip('_')  # Clean up underscores
    
    idea_log_dir = os.path.join(model_log_dir, safe_idea)
    os.makedirs(idea_log_dir, exist_ok=True)
    
    # Create log file with timestamp if not specified
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if log_file is None:
        log_file = os.path.join(idea_log_dir, f"run_{timestamp}.log")
    else:
        # If log_file is specified, still put it in the organized directory
        log_file = os.path.join(idea_log_dir, os.path.basename(log_file))
    
    # Create summary file for this run
    summary_file = os.path.join(idea_log_dir, f"summary_{timestamp}.txt")
    
    logger.info(f"Log directory structure: {base_log_dir}/{model_type.lower()}/{safe_idea}/")
    logger.info(f"Log file: {log_file}")
    logger.info(f"Current working directory: {os.getcwd()}")
    
    # Try to write to the log file
    try:
        # Write initial header to log file
        with open(log_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("MetaGPT Multi-Agent Execution Log\n")
            f.write("="*80 + "\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(f"Model Type: {model_type}\n")
            f.write(f"Idea: {idea}\n")
            f.write(f"Investment: {investment}\n")
            f.write(f"Rounds: {n_round}\n")
            f.write(f"Human Review: {add_human}\n")
            f.write("="*80 + "\n\n")
        
        # Write summary info
        with open(summary_file, 'w') as f:
            f.write(f"Run Summary\n")
            f.write(f"="*40 + "\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(f"Model: {model_type}\n")
            f.write(f"Idea: {idea}\n")
            f.write(f"Investment: {investment}\n")
            f.write(f"Rounds: {n_round}\n")
            f.write(f"Human Review: {add_human}\n")
            f.write(f"Log File: {os.path.basename(log_file)}\n")
            f.write("="*40 + "\n")
        
        logger.info(f"Successfully created log file at {log_file}")
        logger.info(f"Summary file created at {summary_file}")
    except Exception as e:
        logger.error(f"Cannot write to log location: {e}")
        # Fallback to simple location
        log_file = os.path.join(os.getcwd(), f"agent_log_{timestamp}.txt")
        logger.info(f"Falling back to log file at: {log_file}")
    
    # Configure LLM based on model_type parameter
    llm_config = LLMConfig()
    llm_config.proxy = ""
    
    if model_type.lower() == "qwen":
        # Configure for Qwen model
        llm_config.api_type = LLMType.QWEN
        llm_config.model = "Qwen2.5-Coder-32B-Instruct"
        llm_config.base_url = os.getenv("BASE_URL", "http://localhost:12355/v1")
        llm_config.api_key = os.getenv("OPENAI_API_KEY", "fake-key")
        llm_config.temperature = 0.7
        llm_config.max_token = int(os.getenv("QWEN_MAX_TOKENS", "4096"))
        logger.info(f"Configured for Qwen model: {llm_config.model} at {llm_config.base_url}")
    elif model_type.lower() == "codellama":
        # Configure for CodeLlama model
        llm_config.api_type = LLMType.CODELLAMA
        llm_config.model = "CodeLlama-13b-Instruct"
        llm_config.base_url = os.getenv("BASE_URL", "http://localhost:12355/v1")
        llm_config.api_key = os.getenv("OPENAI_API_KEY", "fake-key")
        llm_config.temperature = 0.7
        llm_config.max_token = int(os.getenv("CODELLAMA_MAX_TOKENS", "2048"))
        logger.info(f"Configured for CodeLlama model: {llm_config.model} at {llm_config.base_url}")
    else:
        # Use default OpenAI configuration
        llm_config.api_key = os.getenv("OPENAI_API_KEY", "sk-")
        llm_config.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        logger.info(f"Using OpenAI model: {llm_config.model}")
    
    # Create context and set the LLM config
    context = Context()
    context.config.llm = llm_config
    
    # Create team with logging enabled
    team = Team(context=context, log_file=log_file)
    team.hire(
        [
            SimpleCoder(context=context),
            SimpleTester(context=context),
            SimpleReviewer(is_human=add_human, context=context),
        ]
    )
    
    team.invest(investment=investment)
    team.run_project(idea)
    await team.run(n_round=n_round)
    
    # Report on created files
    logger.info("="*60)
    logger.info("Execution Complete")
    logger.info("="*60)
    
    # Check if log file was created
    if os.path.exists(log_file):
        logger.info(f"✓ Main log file: {log_file}")
        # Get file size
        file_size = os.path.getsize(log_file)
        logger.info(f"  Size: {file_size:,} bytes")
    else:
        logger.error(f"✗ Log file was not created at {log_file}")
    
    # Check if summary file was created
    if 'summary_file' in locals() and os.path.exists(summary_file):
        logger.info(f"✓ Summary file: {summary_file}")
    
    # Report log directory
    if 'idea_log_dir' in locals():
        logger.info(f"✓ All logs for this idea saved in: {idea_log_dir}")
        # List all files in the directory
        try:
            files = os.listdir(idea_log_dir)
            logger.info(f"  Total files in directory: {len(files)}")
        except Exception as e:
            logger.error(f"  Error listing directory: {e}")


if __name__ == "__main__":
    # Note: This standalone version requires the following pip packages:
    # pip install aiohttp pydantic fire
    fire.Fire(main)