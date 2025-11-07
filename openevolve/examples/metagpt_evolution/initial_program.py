"""
MetaGPT Multi-Agent System for OpenEvolve Evolution
Based on the original standalone_multi_agent.py with EVOLVE-BLOCK markers
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
│ Content Preview: {message.content[:300]}{"..." if len(message.content) > 300 else ""}
└─────────────────────────────────────────────────────────
"""
        self._write_log(message_log)
    
    def log_team_coordination(self, event_type: str, details: str):
        """Log team coordination events"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        message = f"""
┌── TEAM COORDINATION [{timestamp}] ────────────────────────
│ Event: {event_type}
│ Details: {details}
└─────────────────────────────────────────────────────────
"""
        self._write_log(message)
    
    def _write_log(self, message: str):
        """Write message to log file"""
        if self.log_file:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(message + '\n')
            except Exception as e:
                print(f"Logging error: {e}")

class LLMType(Enum):
    OPENAI = "openai"
    QWEN = "qwen"
    CODELLAMA = "codellama"

class LLMConfig:
    def __init__(self):
        self.api_type = LLMType.OPENAI
        self.model = "gpt-4o-mini"
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
        instruct_content: Optional[str] = None
        role: str
        cause_by: str = ""
        sent_from: Optional[str] = None
        sent_to: Optional[str] = None
        send_to: Set[str] = Field(default_factory=set)
        
        def __str__(self):
            return f"Message(role={self.role}, content={self.content[:50]}...)"
else:
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
            return "I'll help you with that task. Let me work on it step by step."
        
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
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result["choices"][0]["message"]["content"]
                    else:
                        return f"LLM API Error: {response.status}"
        except Exception as e:
            return f"LLM Communication Error: {str(e)}"

# EVOLVE-BLOCK-START
# This section contains the evolving multi-agent architecture and coordination logic

# === EVOLVING ARCHITECTURE CONFIGURATION ===
class ArchitectureConfig:
    """Configuration for the evolving multi-agent architecture"""
    def __init__(self):
        # Team composition - can evolve to add/remove agent types
        self.agent_types = [
            {"class": "SimpleCoder", "count": 1, "specialization": "general"},
            {"class": "SimpleTester", "count": 1, "specialization": "unit_testing"},
            {"class": "SimpleReviewer", "count": 1, "specialization": "code_review"}
        ]
        
        # Communication protocol - can evolve
        self.communication_protocol = "sequential"  # Can evolve: broadcast, hierarchical, peer-to-peer
        
        # Workflow pattern - can evolve  
        self.workflow_pattern = "waterfall"  # Can evolve: agile, parallel, iterative
        
        # Coordination strategy - can evolve
        self.coordination_strategy = "centralized"  # Can evolve: distributed, market-based, consensus

# === EVOLVING AGENT CAPABILITIES ===
class EvolvingAction(ABC):
    """Base action with evolving capabilities"""
    def __init__(self, context=None, **kwargs):
        self.context = context
        self.llm = LLMInterface(context.config.llm) if context else None
        self.name = self.__class__.__name__
        # Evolving action parameters
        self.creativity_level = kwargs.get('creativity_level', 0.7)
        self.detail_level = kwargs.get('detail_level', 'standard')
        self.specialization = kwargs.get('specialization', 'general')
    
    async def _aask(self, prompt: str, system_msg: str) -> str:
        """LLM interaction with tracing"""
        if not self.llm:
            return "AI response simulated"
        
        messages = [{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}]
        
        if self.context and self.context.tracer:
            trace_id = self.context.tracer.get_next_trace_id()
            response = await self.llm.ask(messages)
            self.context.tracer.log_llm_interaction(trace_id, self.name, prompt, response)
            return response
        else:
            return await self.llm.ask(messages)

class EvolvingCodeAction(EvolvingAction):
    """Evolving code generation action"""
    async def run(self, context: str, **kwargs) -> str:
        # Evolving prompt based on specialization
        if self.specialization == "algorithms":
            system_msg = "You are an expert algorithms engineer focused on efficient, optimal solutions."
            requirements = "Focus on algorithmic efficiency, time/space complexity, and elegant solutions."
        elif self.specialization == "ui":
            system_msg = "You are a UI/UX focused developer creating intuitive interfaces."
            requirements = "Focus on user experience, accessibility, and clean interface design."
        else:
            system_msg = "You are an expert Python programmer."
            requirements = "Write clean, functional Python code with proper error handling."
        
        prompt = f"""
Write Python code for: {context}

Requirements:
{requirements}
- Include comments explaining key logic
- Make the code production-ready
- Detail level: {self.detail_level}

Provide only the code without explanation.
"""
        
        if self.context and self.context.tracer:
            self.context.tracer.log_agent_action_start(self.name, "GenerateCode", context)
        
        return await self._aask(prompt, system_msg)

class EvolvingTestAction(EvolvingAction):
    """Evolving test generation action"""
    async def run(self, context: str, **kwargs) -> str:
        # Evolving test strategy
        if self.specialization == "security_testing":
            system_msg = "You are a security testing expert focused on finding vulnerabilities."
            test_focus = "security vulnerabilities, input validation, edge cases"
        elif self.specialization == "performance_testing":
            system_msg = "You are a performance testing expert."
            test_focus = "performance bottlenecks, scalability, resource usage"
        else:
            system_msg = "You are an expert QA engineer."
            test_focus = "functionality, edge cases, error conditions"
        
        prompt = f"""
Write comprehensive tests for: {context}

Focus on: {test_focus}
- Use pytest framework
- Include clear test function names and docstrings
- Detail level: {self.detail_level}

Provide only test code without explanation.
"""
        
        if self.context and self.context.tracer:
            self.context.tracer.log_agent_action_start(self.name, "GenerateTests", context)
        
        return await self._aask(prompt, system_msg)

class EvolvingReviewAction(EvolvingAction):
    """Evolving code review action"""
    async def run(self, context: str, **kwargs) -> str:
        # Evolving review focus
        if self.specialization == "architecture_review":
            system_msg = "You are a senior architect focused on system design and scalability."
            review_focus = "architectural patterns, scalability, maintainability, design principles"
        elif self.specialization == "security_review":
            system_msg = "You are a security expert reviewing for vulnerabilities."
            review_focus = "security vulnerabilities, attack vectors, secure coding practices"
        else:
            system_msg = "You are a senior software engineer conducting thorough code review."
            review_focus = "code quality, best practices, potential bugs, test coverage"
        
        prompt = f"""
Review the following code and tests: {context}

Focus on: {review_focus}
Provide:
1. Overall quality assessment
2. Specific issues found
3. Improvement suggestions
4. Quality rating (1-10)

Be thorough but concise.
"""
        
        if self.context and self.context.tracer:
            self.context.tracer.log_agent_action_start(self.name, "ReviewCode", context)
        
        return await self._aask(prompt, system_msg)

# === EVOLVING AGENT ROLES ===
class EvolvingAgent:
    """Evolving agent with configurable capabilities"""
    def __init__(self, role_type: str, context=None, **kwargs):
        self.role_type = role_type
        self.context = context
        self.name = kwargs.get('name', f"{role_type}_Agent")
        self.specialization = kwargs.get('specialization', 'general')
        self.capabilities = self._init_capabilities(role_type, **kwargs)
        self.memory = []
        self.performance_metrics = {"tasks_completed": 0, "avg_quality": 0.0}
    
    def _init_capabilities(self, role_type: str, **kwargs):
        """Initialize capabilities based on role type - can evolve"""
        if role_type == "SimpleCoder":
            return [EvolvingCodeAction(self.context, specialization=self.specialization)]
        elif role_type == "SimpleTester":
            return [EvolvingTestAction(self.context, specialization=self.specialization)]  
        elif role_type == "SimpleReviewer":
            return [EvolvingReviewAction(self.context, specialization=self.specialization)]
        else:
            return []
    
    def get_context(self) -> str:
        """Get context from memory"""
        if not self.memory:
            return "No previous context"
        return "\n".join([f"{msg.role}: {msg.content[:200]}" for msg in self.memory[-2:]])
    
    async def act(self, message: Optional[Message] = None) -> Optional[Message]:
        """Perform action based on current capabilities"""
        if message:
            self.memory.append(message)
        
        if not self.capabilities:
            return None
        
        context = self.get_context()
        action = self.capabilities[0]  # Use first capability - can evolve to choose best
        
        if self.context and self.context.tracer:
            self.context.tracer.log_team_coordination("AGENT_ACTION", f"{self.name} executing {action.name}")
        
        try:
            result = await action.run(context)
            
            response = Message(
                content=result,
                role=self.role_type,
                cause_by=action.name,
                sent_from=self.name
            )
            
            self.performance_metrics["tasks_completed"] += 1
            return response
            
        except Exception as e:
            error_msg = f"Agent {self.name} error: {str(e)}"
            if self.context and self.context.tracer:
                self.context.tracer.log_team_coordination("AGENT_ERROR", error_msg)
            return None

# === EVOLVING COMMUNICATION PROTOCOLS ===
class EvolvingCommunicationProtocol:
    """Evolving communication and coordination protocols"""
    def __init__(self, protocol_type: str = "sequential"):
        self.protocol_type = protocol_type
        self.message_queue = []
        self.coordination_state = {}
    
    def route_message(self, message: Message, agents: List[EvolvingAgent]) -> List[EvolvingAgent]:
        """Route messages based on evolving protocol"""
        if self.protocol_type == "sequential":
            # Current: sequential execution
            return agents
        elif self.protocol_type == "broadcast":
            # Evolution might discover: broadcast to all agents
            return agents
        elif self.protocol_type == "hierarchical":
            # Evolution might discover: hierarchical routing
            return self._hierarchical_routing(message, agents)
        else:
            return agents
    
    def _hierarchical_routing(self, message: Message, agents: List[EvolvingAgent]) -> List[EvolvingAgent]:
        """Hierarchical message routing - can evolve"""
        # Simple hierarchy: Coder -> Tester -> Reviewer
        if message.cause_by == "ProjectInitiation":
            return [a for a in agents if a.role_type == "SimpleCoder"]
        elif message.cause_by == "EvolvingCodeAction":
            return [a for a in agents if a.role_type == "SimpleTester"]
        elif message.cause_by == "EvolvingTestAction":
            return [a for a in agents if a.role_type == "SimpleReviewer"]
        return []

# === EVOLVING TEAM ORCHESTRATION ===
async def create_evolving_team(context: Context, config: ArchitectureConfig) -> List[EvolvingAgent]:
    """Create team with evolving composition"""
    agents = []
    
    for agent_config in config.agent_types:
        for i in range(agent_config["count"]):
            agent = EvolvingAgent(
                role_type=agent_config["class"],
                context=context,
                name=f"{agent_config['class']}_{i+1}",
                specialization=agent_config["specialization"]
            )
            agents.append(agent)
    
    # Evolution can add specialized agents:
    # if config.add_specialist_agents:
    #     agents.append(EvolvingAgent("SecurityExpert", context, specialization="security_review"))
    #     agents.append(EvolvingAgent("PerformanceAnalyst", context, specialization="performance_testing"))
    
    return agents

async def execute_evolving_workflow(agents: List[EvolvingAgent], idea: str, config: ArchitectureConfig, tracer: ExecutionTracer) -> str:
    """Execute the evolving workflow"""
    tracer.log_team_coordination("WORKFLOW_START", f"Executing {config.workflow_pattern} workflow with {len(agents)} agents")
    
    # Initialize communication protocol
    comm_protocol = EvolvingCommunicationProtocol(config.communication_protocol)
    
    # Create initial message
    initial_msg = Message(
        content=f"Project requirement: {idea}",
        instruct_content=idea,
        role="ProjectManager", 
        cause_by="ProjectInitiation"
    )
    
    messages = [initial_msg]
    
    # Execute workflow based on pattern
    if config.workflow_pattern == "waterfall":
        # Sequential execution - current approach
        current_msg = initial_msg
        for agent in agents:
            response = await agent.act(current_msg)
            if response:
                messages.append(response)
                current_msg = response
                tracer.log_team_coordination("MESSAGE_FLOW", f"Message from {agent.name} to next agent")
    
    elif config.workflow_pattern == "parallel":
        # Parallel execution - evolution might discover
        tasks = [agent.act(initial_msg) for agent in agents]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        messages.extend([r for r in responses if isinstance(r, Message)])
        
    elif config.workflow_pattern == "iterative":
        # Iterative refinement - evolution might discover
        for iteration in range(3):  # 3 iterations
            round_messages = []
            for agent in agents:
                last_msg = messages[-1] if messages else initial_msg
                response = await agent.act(last_msg)
                if response:
                    round_messages.append(response)
            messages.extend(round_messages)
            tracer.log_team_coordination("ITERATION_COMPLETE", f"Iteration {iteration+1} completed")
    
    total_messages = len(messages)
    tracer.log_team_coordination("WORKFLOW_END", f"Workflow completed with {total_messages} messages")
    
    return f"Evolving multi-agent system completed {config.workflow_pattern} workflow with {total_messages} messages"

# === MAIN EVOLVING COORDINATION FUNCTION ===
async def run_evolving_multi_agent_system(idea: str, context: Context, tracer: ExecutionTracer, n_rounds: int = 3) -> str:
    """Main coordination function with evolving architecture"""
    
    # Initialize evolving architecture configuration
    arch_config = ArchitectureConfig()
    
    tracer.log_team_coordination("SYSTEM_START", f"Starting evolving multi-agent system: {arch_config.communication_protocol} protocol, {arch_config.workflow_pattern} workflow")
    
    # Create evolving team
    agents = await create_evolving_team(context, arch_config)
    
    # Execute evolving workflow
    result = await execute_evolving_workflow(agents, idea, arch_config, tracer)
    
    return result

# EVOLVE-BLOCK-END

# Fixed execution interface (not evolved)
async def run_multi_agent_task(idea: str, n_rounds: int = 3, log_file: str = None):
    """Run a multi-agent task and return the execution trace"""
    # Create context with LLM configuration
    context = Context()
    context.config.llm.api_key = os.getenv("OPENAI_API_KEY", "fake-key")
    context.config.llm.model = "gpt-4o-mini"
    
    # Create execution tracer
    tracer = ExecutionTracer(log_file)
    context.tracer = tracer
    
    # Run the evolving multi-agent system
    result = await run_evolving_multi_agent_system(idea, context, tracer, n_rounds)
    
    # Return the trace content for evaluation
    if log_file and os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            return f.read()
    return result