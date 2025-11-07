"""
Filename: MetaGPT/examples/build_customized_multi_agents.py
Created Date: Wednesday, November 15th 2023, 7:12:39 pm
Author: garylin2099
"""
import re
import os

import fire


import sys

sys.path.append("/home/mert/mlsys/meta_gpt/MetaGPT/metagpt")

from metagpt.actions import Action, UserRequirement
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.team import Team
from metagpt.configs.llm_config import LLMConfig
# from metagpt.config import CONFIG  # Import the global config object
from metagpt.context import Context
# Import all providers to ensure they're registered
import metagpt.provider

import json



def parse_code(rsp):
    pattern = r"```python(.*)```"
    match = re.search(pattern, rsp, re.DOTALL)
    code_text = match.group(1) if match else rsp
    return code_text


class SimpleWriteCode(Action):
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
    name: str = "Alice"
    profile: str = "SimpleCoder"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._watch([UserRequirement])
        self.set_actions([SimpleWriteCode])


class SimpleWriteTest(Action):
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
    name: str = "Bob"
    profile: str = "SimpleTester"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteTest])
        self._watch([SimpleWriteCode, SimpleWriteReview])

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: to do {self.rc.todo}({self.rc.todo.name})")
        todo = self.rc.todo

        # Collect context
        context = self.get_memories()

        # Perform action and get result
        code_text = await todo.run(context, k=5)
        msg = Message(content=code_text, role=self.profile, cause_by=type(todo))

        # Save trace
        trace = {
            "role": self.profile,
            "action": type(todo).__name__,
            "context": context,
            "output": code_text,
        }
        # with open("traces.json", "a") as f:
        #     f.write(json.dumps(trace) + "\n")

        return msg


class SimpleWriteReview(Action):
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
    name: str = "Charlie"
    profile: str = "SimpleReviewer"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([SimpleWriteReview])
        self._watch([SimpleWriteTest])


async def main(
    idea: str = "write a function that calculates the product of a list",
    investment: float = 3.0,
    n_round: int = 5,
    add_human: bool = False,
    log_file: str = "agent_communication.txt",
    model_type: str = "openai",
):
    # Convert to absolute path
    log_file = os.path.abspath(log_file)
    logger.info(f"Log file will be saved to: {log_file}")
    logger.info(f"Current working directory: {os.getcwd()}")
    
    # Create a direct log file to verify we can write to the location
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            logger.info(f"Created log directory: {log_dir}")
        
        # Test if we can write to this location
        with open(log_file, 'w') as f:
            f.write("=== Test write to log file ===\n")
        logger.info(f"Successfully created test log file at {log_file}")
    except Exception as e:
        logger.error(f"Cannot write to specified log location: {e}")
        # Fall back to current directory
        log_file = os.path.join(os.getcwd(), "agent_communication.txt")
        logger.info(f"Falling back to log file at: {log_file}")
        # Test the fallback location
        try:
            with open(log_file, 'w') as f:
                f.write("=== Test write to fallback log file ===\n")
            logger.info(f"Successfully created test log file at fallback location")
        except Exception as e2:
            logger.error(f"Cannot write to fallback location either: {e2}")
            log_file = None
    
    # Disable proxies at the environment level
    if "http_proxy" in os.environ:
        del os.environ["http_proxy"]
    if "https_proxy" in os.environ:
        del os.environ["https_proxy"]
    
    # Configure LLM based on model_type parameter
    llm_config = LLMConfig()
    llm_config.proxy = ""  # Empty string instead of None
    
    if model_type.lower() == "qwen":
        # Configure for Qwen model
        from metagpt.configs.llm_config import LLMType
        llm_config.api_type = LLMType.QWEN
        llm_config.model = "Qwen2.5-Coder-32B-Instruct"
        llm_config.base_url = os.getenv("BASE_URL", "http://localhost:12355/v1")
        llm_config.api_key = os.getenv("OPENAI_API_KEY", "fake-key")
        llm_config.temperature = 0.7
        llm_config.max_token = int(os.getenv("QWEN_MAX_TOKENS", "4096"))
        logger.info(f"Configured for Qwen model: {llm_config.model} at {llm_config.base_url}")
    elif model_type.lower() == "codellama":
        # Configure for CodeLlama model
        from metagpt.configs.llm_config import LLMType
        llm_config.api_type = LLMType.CODELLAMA
        llm_config.model = "CodeLlama-13b-Instruct"
        llm_config.base_url = os.getenv("BASE_URL", "http://localhost:12355/v1")
        llm_config.api_key = os.getenv("OPENAI_API_KEY", "fake-key")
        llm_config.temperature = 0.7
        llm_config.max_token = int(os.getenv("CODELLAMA_MAX_TOKENS", "2048"))
        logger.info(f"Configured for CodeLlama model: {llm_config.model} at {llm_config.base_url}")
    else:
        # Use default configuration from config2.yaml for other models
        logger.info(f"Using default model configuration for: {model_type}")

    # Create context and set the LLM config properly
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
    
    # Check if log file was created
    if log_file and os.path.exists(log_file):
        logger.info(f"Agent communication has been logged to {log_file}")
        # Print the first few lines to confirm content
        try:
            with open(log_file, 'r') as f:
                content = f.read(200)
                logger.info(f"Log file preview: {content}")
        except Exception as e:
            logger.error(f"Error reading log file: {e}")
    elif log_file:
        logger.error(f"Log file was not created at {log_file}")
    else:
        logger.error("Logging was disabled due to file write errors")


if __name__ == "__main__":
    logger.add("trace_logs.log", rotation="10 MB")
    fire.Fire(main)
