# MetaGPT Multi-Agent System Evolution

Use OpenEvolve to automatically improve the sophisticated MetaGPT multi-agent coordination patterns by minimizing failure modes.

## What It Does

1. Runs the MetaGPT multi-agent system on programming tasks
2. Captures rich execution traces with comprehensive logging
3. Uses MAST LLM judge to detect 14 types of failure modes
4. Evolves the sophisticated agent coordination logic to minimize failures

## Key Features

- **Rich MetaGPT Architecture**: Uses original MetaGPT implementation with sophisticated tracing and coordination
- **Comprehensive Logging**: ExecutionTracer with detailed agent interaction logs
- **Advanced Role System**: SimpleCoder, SimpleTester, SimpleReviewer with rich actions
- **MAST Evaluation**: Detects role confusion, task derailment, coordination breakdowns

## Setup

```bash
cd examples/metagpt_evolution
export OPENAI_API_KEY="your-key"
```

## Run Evolution

```bash
cd /path/to/openevolve
python openevolve-run.py examples/metagpt_evolution/initial_program.py \
                         examples/metagpt_evolution/evaluator.py \
                         --config examples/metagpt_evolution/config.yaml \
                         --iterations 50
```

## Expected Evolution

OpenEvolve can discover architectural improvements like:

### Agent Composition Evolution
- **Add/Remove Agent Types**: Start with Coder/Tester/Reviewer, evolve to include SecurityExpert, PerformanceAnalyst, etc.
- **Agent Specialization**: Evolve from "general" to specialized roles (algorithms, UI, security_testing, architecture_review)
- **Team Size Optimization**: Discover optimal number of each agent type

### Communication Protocol Evolution  
- **Sequential** → **Hierarchical** → **Broadcast** → **Peer-to-Peer**
- **Message Routing**: Evolve intelligent message routing based on content and agent capabilities
- **Coordination Patterns**: Discover consensus, auction-based, or market-driven coordination

### Workflow Pattern Evolution
- **Waterfall** → **Parallel** → **Iterative** → **Hybrid** workflows
- **Execution Strategies**: Discover when to use parallel vs sequential execution
- **Feedback Loops**: Evolve sophisticated iteration and refinement patterns

### Capability Evolution
- **Action Specialization**: Evolve from basic code/test/review to domain-specific actions
- **Dynamic Role Assignment**: Evolve agents that can switch roles based on task needs
- **Performance-Based Selection**: Evolve systems that choose best agent for each task

## Evolving Architecture Components

### Inside EVOLVE-BLOCK:
- `ArchitectureConfig`: Team composition, communication protocols, workflow patterns
- `EvolvingAgent`: Agent creation with configurable specializations and capabilities  
- `EvolvingCommunicationProtocol`: Message routing and coordination strategies
- `create_evolving_team()`: Dynamic team composition based on configuration
- `execute_evolving_workflow()`: Workflow execution with multiple pattern options

### Outside EVOLVE-BLOCK (Fixed Infrastructure):
- `ExecutionTracer`: Rich logging and tracing system
- `Context Management`: Configuration and state management
- `LLMInterface`: Async communication with error handling
- `Message`: Core communication structure

This enables evolution of the **what** (architecture) while preserving the **how** (infrastructure).