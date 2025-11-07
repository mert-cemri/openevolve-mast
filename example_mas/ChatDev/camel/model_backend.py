# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========

# Fix tokenizer parallelism warning before any imports
import os
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

import openai
import tiktoken

from camel.typing import ModelType
from chatdev.statistics import prompt_cost
from chatdev.utils import log_visualize

try:
    from openai.types.chat import ChatCompletion
    from openai.types.chat.chat_completion import Choice
    from openai.types.chat.chat_completion_message import ChatCompletionMessage
    from openai.types.completion_usage import CompletionUsage

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version

# Add Anthropic imports
try:
    import anthropic
    from anthropic.types import MessageParam # For typing Claude messages
except ImportError:
    anthropic = None # type: ignore
    MessageParam = None # type: ignore

from camel.messages import BaseMessage
from camel.typing import (
    ModelType,
    RoleType,
    ChatMessage,
    Choice,
    ModelResponse,
    Usage,
)

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') # Use .get for safety
if 'BASE_URL' in os.environ:
    BASE_URL = os.environ['BASE_URL']
else:
    BASE_URL = None


class BaseModelBackend(ABC):
    r"""Base class for all model backends."""

    def __init__(self, model_type: ModelType,
                 model_config_dict: Dict[str, Any]) -> None:
        self.model_type = model_type
        self.model_config_dict = model_config_dict

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        r"""Runs the model backend."""
        pass

    @property
    def token_limit(self) -> int:
        r"""Returns the token limit of the model.

        Raises:
            NotImplementedError: If the token limit for the model is not
                implemented.

        Returns:
            int: The token limit of the model.
        """
        if self.model_type == ModelType.GPT_3_5_TURBO:
            return 4096
        elif self.model_type == ModelType.GPT_3_5_TURBO_16K:
            return 16384
        elif self.model_type == ModelType.GPT_4:
            return 8192
        elif self.model_type == ModelType.GPT_4_32k:
            return 32768
        elif self.model_type == ModelType.GPT_4_TURBO:
            # return 128000 # Official, but ChatDev uses 100k in some places
            return 100000
        elif self.model_type == ModelType.GPT_4_TURBO_PREVIEW:
            return 128000
        elif self.model_type == ModelType.GPT_4_VISION_PREVIEW: # context window for text
            return 128000
        elif self.model_type == ModelType.GPT_4O:
            return 128000
        elif self.model_type == ModelType.GPT_4O_MINI:
            return 128000 # Assuming same as GPT-4o, adjust if different
        elif self.model_type == ModelType.STUB:
            return 4096
        elif self.model_type == ModelType.CLAUDE:
            # This needs to be model specific for Claude, e.g. claude-3-opus-20240229 is 200K
            # For now, a general high value, or make it configurable via ClaudeModel
            return 200000
        elif self.model_type == ModelType.QWEN_2_5_CODER_32B:
            # Qwen2.5-Coder-32B-Instruct typically has 32K context window
            return 32768
        elif self.model_type == ModelType.CODELLAMA_13B_INSTRUCT:
            # CodeLlama-13b-Instruct typically has 16K context window (configurable via env vars)
            return 16384
        raise NotImplementedError(f"Token limit for model {self.model_type} is not implemented.")

    @property
    def stream(self) -> bool:
        r"""Returns whether the model is in stream mode.
        In stream mode, the model will return tokens one by one.
        Otherwise, the model will return all tokens at once.

        Returns:
            bool: Whether the model is in stream mode.
        """
        return self.model_config_dict.get('stream', False)


class OpenAIModel(BaseModelBackend):
    r"""OpenAI API in a unified ModelBackend interface."""

    def __init__(self, model_type: ModelType, model_config_dict: Dict) -> None:
        super().__init__(model_type, model_config_dict)
        # self.model_config_dict here is the one from ModelFactory,
        # typically from ChatChainConfig.json

    def run(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        # kwargs comes from ChatAgent.step() and includes 'messages'
        # and all other model parameters (temperature, top_p, etc.)
        # from the agent's self.model_config (e.g., ChatGPTConfig).

        params_for_api = kwargs.copy() # Work with a mutable copy

        current_messages = params_for_api.pop("messages", None)
        if not current_messages:
            raise ValueError("Messages not found in parameters for OpenAIModel.run")

        # Calculate num_prompt_tokens using the model's tiktoken encoding
        # Use the value_for_tiktoken property from ModelType for accuracy
        try:
            encoding = tiktoken.encoding_for_model(self.model_type.value_for_tiktoken)
        except KeyError:
            # Fallback for models not directly supported by tiktoken's model name mapping
            encoding = tiktoken.get_encoding("cl100k_base")

        # This is a simplified token counting for the prompt.
        # For higher accuracy, especially if ChatML format is strictly followed,
        # a more detailed counting function (like num_tokens_from_messages in camel.utils)
        # should be used. However, this calculation is internal to OpenAIModel.run
        # for determining max_completion_tokens.
        # The ChatAgent already calculates a more precise num_tokens for other purposes.
        prompt_content_for_count = "\n".join([msg["content"] for msg in current_messages])
        num_prompt_tokens = len(encoding.encode(prompt_content_for_count))
        
        # Adding a buffer for message roles and structure, this is an approximation.
        # OpenAI's official guidance involves counting tokens for roles, names, and control characters.
        # A fixed per-message overhead is a common heuristic.
        num_prompt_tokens += 4 * len(current_messages) # Rough overhead per message
        num_prompt_tokens += 2 # For priming the assistant's reply

        if openai_new_api:
            if BASE_URL:
                client = openai.OpenAI(api_key=OPENAI_API_KEY, base_url=BASE_URL)
            else:
                client = openai.OpenAI(api_key=OPENAI_API_KEY)

            # This map should represent the TOTAL CONTEXT WINDOW of the models.
            num_max_token_map = {
                "gpt-3.5-turbo": 4096,
                "gpt-3.5-turbo-16k": 16384,
                "gpt-3.5-turbo-0613": 4096, # Often alias for gpt-3.5-turbo
                "gpt-3.5-turbo-16k-0613": 16384, # Often alias for gpt-3.5-turbo-16k
                "gpt-4": 8192,
                "gpt-4-0613": 8192, # Often alias for gpt-4
                "gpt-4-32k": 32768,
                "gpt-4-turbo": 128000, # Corrected
                "gpt-4o": 128000,      # Corrected
                "gpt-4o-mini": 128000, # Assuming same as gpt-4o, needs verification if different
            }
            
            model_total_context = num_max_token_map.get(self.model_type.value)
            if model_total_context is None:
                # Fallback to the token_limit property if model not in specific map
                try:
                    model_total_context = self.token_limit
                except NotImplementedError:
                    raise ValueError(
                        f"Model {self.model_type.value} not found in num_max_token_map and token_limit not defined."
                    )
            
            # Calculate available tokens for completion based on total context
            max_completion_tokens = model_total_context - num_prompt_tokens

            if max_completion_tokens <= 0:
                raise ValueError(
                    f"Prompt is too long for model {self.model_type.value}. "
                    f"Prompt tokens: {num_prompt_tokens}, Model total context: {model_total_context}. "
                    f"Need at least 1 token for completion."
                )

            # NEW: Model-specific inherent maximum *completion* tokens
            # These are typical output limits, which are often smaller than total context.
            model_inherent_max_output_map = {
                "gpt-4o": 16384,          # Based on the API error message you received
                "gpt-4-turbo": 4096,      # Common output limit for GPT-4 Turbo
                "gpt-4": 4096,            # Common output limit for GPT-4
                "gpt-4o-mini": 8192,      # Example: GPT-4o mini might have a smaller output cap
                "gpt-3.5-turbo": 4096,    # Common output limit for GPT-3.5 Turbo
                "gpt-3.5-turbo-16k": 4096 # Even with larger context, output may be capped
                # Add other models as needed with their specific *max output* token limits
            }
            # Default inherent max output if model not in map
            default_inherent_max_output = 4096 
            model_inherent_max_output = model_inherent_max_output_map.get(
                self.model_type.value, default_inherent_max_output
            )

            # First, cap by the model's inherent maximum output capability
            max_completion_tokens = min(max_completion_tokens, model_inherent_max_output)

            # Then, respect user-configured 'max_tokens' from ChatGPTConfig if it's even smaller
            user_configured_max_output = params_for_api.get('max_tokens')
            if user_configured_max_output is not None:
                try:
                    user_configured_max_output = int(user_configured_max_output)
                    if user_configured_max_output > 0:
                         max_completion_tokens = min(max_completion_tokens, user_configured_max_output)
                except (ValueError, TypeError):
                    # Log this ideally, but for now, pass to not break execution
                    print(f"Warning: Invalid 'max_tokens' value ('{user_configured_max_output}') in agent config. Ignoring it for capping.")


            # Ensure max_completion_tokens is at least 1 if prompt nearly fills context
            if max_completion_tokens <= 0:
                # This case should ideally be caught earlier, but as a safeguard:
                # If after all capping, it's non-positive, it means prompt + desired/inherent output > total context
                # Or the prompt itself is too large. The earlier check for max_completion_tokens <= 0 handles prompt too large.
                # This handles if model_inherent_max_output or user_configured_max_output is too large for remaining space.
                # For now, let's ensure it's at least a small positive number if possible, or let the API error.
                # A more robust solution might be to error out here if it's still <=0 after considering output caps.
                # However, the API will error if max_tokens is not positive.
                # The most important thing is that it's not excessively large.
                # If it became non-positive due to capping, it implies an issue.
                # For safety, if it's non-positive, we might rely on the API to error or set a minimum like 1.
                # But the previous check (max_completion_tokens <= 0 before capping) should handle prompt too long.
                # This path (<=0 after capping) means the requested/inherent output itself is an issue.
                 print(f"Warning: Calculated max_completion_tokens is {max_completion_tokens} after all capping. "
                       f"Model: {self.model_type.value}, Prompt Tokens: {num_prompt_tokens}, Total Context: {model_total_context}")
                 # Ensure it's at least 1, though the API might still reject if prompt is truly too big.
                 if max_completion_tokens <=0 : max_completion_tokens = 1


            params_for_api['max_tokens'] = max_completion_tokens
            
            # Ensure 'stream' parameter is correctly passed if it's part of the config
            if 'stream' not in params_for_api and hasattr(self, 'stream'):
                 params_for_api['stream'] = self.stream


            response = client.chat.completions.create(
                messages=current_messages,
                model=self.model_type.value,
                **params_for_api  # Contains temperature, top_p, and now corrected max_tokens
            )
            return response.model_dump() # Standard way to get dict from Pydantic model
        else:
            # Handle old API if necessary, or remove if fully deprecated
            raise NotImplementedError("Old OpenAI API support is not fully maintained.")


class StubModel(BaseModelBackend):
    r"""A dummy model used for unit tests."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs) -> Dict[str, Any]:
        ARBITRARY_STRING = "Lorem Ipsum"

        return dict(
            id="stub_model_id",
            usage=dict(),
            choices=[
                dict(finish_reason="stop",
                     message=dict(content=ARBITRARY_STRING, role="assistant"))
            ],
        )


class ClaudeModel(BaseModelBackend):
    r"""Claude API model backend.

    Args:
        model_type (ModelType): The type of the model (should be ModelType.CLAUDE).
        model_config_dict (Dict[str, Any]): A dictionary containing
            the model configuration. Must include "api_key" and can include
            "model" (e.g., "claude-3-opus-20240229"), "temperature",
            "max_tokens", "top_p", "top_k", "stop_sequences".
    """

    def __init__(self, model_type: ModelType, model_config_dict: Dict[str, Any]) -> None:
        super().__init__(model_type, model_config_dict)
        if anthropic is None:
            raise ImportError("Anthropic SDK not installed. Please install with `pip install anthropic`.")

        self.api_key = self.model_config_dict.get("api_key") or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            # In a production scenario, you might want to raise an error if the API key is truly missing.
            # For now, let's assume the hardcoded key was a temporary measure during development.
            # If you intend to always use a hardcoded key, it should be managed securely.
            print("Warning: Anthropic API key not found via config or ANTHROPIC_API_KEY env var.")
            # Reverting to the previous behavior of raising an error if no key is found.
            raise ValueError(
                "Anthropic API key not found. Set ANTHROPIC_API_KEY "
                "environment variable or pass 'api_key' in model_config_dict."
            )

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model_name = self.model_config_dict.get("model", "claude-3-sonnet-20240229")
        
        self.temperature = self.model_config_dict.get("temperature")
        config_max_tokens = self.model_config_dict.get("max_tokens")
        if config_max_tokens is None:
            self.max_tokens_to_generate = 4096
        else:
            try:
                self.max_tokens_to_generate = int(config_max_tokens)
                if self.max_tokens_to_generate <= 0:
                    print(f"Warning: 'max_tokens' value '{config_max_tokens}' is not positive. Using default 4096.")
                    self.max_tokens_to_generate = 4096
            except (ValueError, TypeError):
                print(f"Warning: Invalid 'max_tokens' value '{config_max_tokens}' in config. Using default 4096.")
                self.max_tokens_to_generate = 4096
        
        self.top_p = self.model_config_dict.get("top_p")
        self.top_k = self.model_config_dict.get("top_k")
        self.stop_sequences = self.model_config_dict.get("stop_sequences")

    def run(self, *args, **kwargs) -> Dict[str, Any]:
        messages_from_agent = kwargs.get("messages", []) # messages from ChatAgent.step
        
        # Claude specific message formatting
        anthropic_messages: List[MessageParam] = []
        system_prompt_parts = []

        for msg in messages_from_agent:
            if msg["role"] == "system":
                system_prompt_parts.append(msg["content"])
            elif msg["role"] == "user":
                anthropic_messages.append({"role": "user", "content": msg["content"]})
            elif msg["role"] == "assistant":
                anthropic_messages.append({"role": "assistant", "content": msg["content"]})

        # Build API parameters using ClaudeModel's initialized config,
        # but allow overrides from ChatAgent's config if they were passed in kwargs
        # For Claude, the ChatAgent's config (temperature, etc.) is in kwargs.
        # The ClaudeModel's self.temperature etc. are from its own init_model_config_dict.
        # We should decide which takes precedence or how to merge.
        # For consistency with OpenAIModel, let's allow kwargs from ChatAgent to override.
        
        final_api_params: Dict[str, Any] = {
            "model": self.model_name,
            "messages": anthropic_messages,
            "max_tokens": self.max_tokens_to_generate, # Default from ClaudeModel init
        }

        if system_prompt_parts:
            final_api_params["system"] = "\n".join(system_prompt_parts)

        # Override with parameters from ChatAgent's config if present in kwargs
        # These are parameters like temperature, top_p, top_k, etc.
        # Note: 'max_tokens' from ChatAgent's kwargs is not directly used here for Claude,
        # as ClaudeModel uses self.max_tokens_to_generate. If dynamic calculation is needed
        # for Claude like for OpenAI, this part would need adjustment.
        # For now, we use ClaudeModel's initialized self.max_tokens_to_generate.
        
        # Parameters from ChatAgent's config (passed in kwargs)
        agent_temperature = kwargs.get("temperature", self.temperature)
        agent_top_p = kwargs.get("top_p", self.top_p)
        agent_top_k = kwargs.get("top_k", self.top_k)
        # 'max_tokens' from agent's kwargs could also be considered if needed:
        # agent_max_tokens = kwargs.get("max_tokens", self.max_tokens_to_generate)
        # final_api_params["max_tokens"] = agent_max_tokens
        
        if agent_temperature is not None:
            final_api_params["temperature"] = agent_temperature
        if agent_top_p is not None:
            final_api_params["top_p"] = agent_top_p
        if agent_top_k is not None:
            final_api_params["top_k"] = agent_top_k
        
        # stop_sequences from ClaudeModel's init
        if self.stop_sequences is not None:
            if isinstance(self.stop_sequences, list) and all(isinstance(s, str) for s in self.stop_sequences):
                final_api_params["stop_sequences"] = self.stop_sequences
            else:
                print(f"Warning: 'stop_sequences' in ClaudeModel config is not a list of strings: {self.stop_sequences}. Ignoring.")
        
        try:
            response = self.client.messages.create(**final_api_params)
            
            return {
                "id": response.id,
                "model": self.model_type.value, # Add model to response
                "choices": [{
                    "message": {
                        "role": "assistant",
                        "content": "".join([block.text for block in response.content if block.type == "text"])
                    },
                    "finish_reason": response.stop_reason
                }],
                "usage": {
                    "prompt_tokens": response.usage.input_tokens,
                    "completion_tokens": response.usage.output_tokens,
                    "total_tokens": response.usage.input_tokens + response.usage.output_tokens
                }
            }
        except Exception as e:
            # Log the parameters that caused the error for easier debugging
            # print(f"Error during Claude API call with params: {final_api_params}")
            raise RuntimeError(f"Error during Claude API call: {e}")


class QwenModel(BaseModelBackend):
    r"""Qwen API model backend using completions endpoint.
    
    This backend is designed for locally hosted Qwen models served via vLLM
    with OpenAI-compatible API using the completions endpoint.
    
    Args:
        model_type (ModelType): The type of the model (should be ModelType.QWEN_2_5_CODER_32B).
        model_config_dict (Dict): Configuration dictionary containing API settings
            like "api_key", "base_url", "temperature", etc.
    """

    def __init__(self, model_type: ModelType, model_config_dict: Dict[str, Any]) -> None:
        super().__init__(model_type, model_config_dict)
        
        # Debug: print what's in the config dict
        print(f"QwenModel config dict: {model_config_dict}")
        
        # Get API configuration
        self.api_key = self.model_config_dict.get("api_key") or os.getenv("OPENAI_API_KEY") or "fake-key"
        self.base_url = self.model_config_dict.get("base_url") or os.getenv("BASE_URL") or "http://localhost:12355/v1"
        
        # Make max_tokens configurable as hyperparameter
        self.model_max_tokens = int(os.getenv("QWEN_MAX_TOKENS", "30208"))  # User-specified max tokens
        self.context_window = int(os.getenv("QWEN_CONTEXT_WINDOW", str(self.model_max_tokens)))  # Total context window
        
        # Initialize OpenAI client with explicit parameter handling to avoid proxies issue
        try:
            # Try with base_url first
            import httpx
            http_client = httpx.Client()
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
                http_client=http_client
            )
        except Exception as e:
            print(f"Error with custom http client: {e}")
            try:
                # Try without custom http client
                self.client = openai.OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url
                )
            except Exception as e2:
                print(f"Error with base_url: {e2}")
                try:
                    # Last resort: minimal client without base_url
                    print("Falling back to minimal OpenAI client")
                    self.client = openai.OpenAI(
                        api_key=self.api_key
                    )
                    # Override base_url manually if needed
                    if self.base_url and hasattr(self.client, '_base_url'):
                        self.client._base_url = self.base_url
                except Exception as e3:
                    print(f"All OpenAI client initialization methods failed: {e3}")
                    raise RuntimeError(f"Cannot initialize OpenAI client: {e3}")
        
        self.model_name = self.model_config_dict.get("model", self.model_type.value)
        self.temperature = self.model_config_dict.get("temperature", 0.7)  # Increase for more creativity
        self.max_tokens = self.model_config_dict.get("max_tokens") or min(4096, self.model_max_tokens // 4)  # Default to 1/4 of context for completion
        
        # Initialize Qwen tokenizer
        try:
            from transformers import AutoTokenizer
            # Use Qwen2.5-1.5B-Instruct for tokenizer (smaller model, same tokenizer)
            self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct", trust_remote_code=True)
            self.use_qwen_tokenizer = True
            print("✅ Loaded Qwen tokenizer successfully")
        except Exception as e:
            print(f"⚠️  Could not load Qwen tokenizer ({e}), falling back to tiktoken approximation")
            self.tokenizer = None
            self.use_qwen_tokenizer = False

    def _count_tokens(self, text: str) -> int:
        """Count tokens using Qwen tokenizer or fallback to tiktoken."""
        if self.use_qwen_tokenizer and self.tokenizer:
            # Use the proper Qwen tokenizer
            return len(self.tokenizer.encode(text))
        else:
            # Fallback to tiktoken approximation
            try:
                encoding = tiktoken.encoding_for_model(self.model_type.value_for_tiktoken)
            except KeyError:
                encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))

    def run(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """Run the Qwen model using completions API."""
        
        params_for_api = kwargs.copy()
        current_messages = params_for_api.pop("messages", None)
        
        if not current_messages:
            raise ValueError("Messages not found in parameters for QwenModel.run")
        
        # Convert messages array to a single prompt string
        prompt = self._convert_messages_to_prompt(current_messages)
        
        # Calculate token limits using proper Qwen tokenizer
        num_prompt_tokens = self._count_tokens(prompt)
        
        # Set token limits for Qwen model (use actual server limit)
        model_total_context = self.context_window # Use the configurable context window
        max_completion_tokens = model_total_context - num_prompt_tokens
        
        # If prompt is too long, truncate messages
        if max_completion_tokens <= 100:  # Need at least 100 tokens for completion
            print(f"⚠️  Prompt too long ({num_prompt_tokens} tokens), truncating messages...")
            print(f"   Model context window: {model_total_context}, Prompt tokens: {num_prompt_tokens}")
            
            # Keep system message and recent messages
            truncated_messages = []
            if current_messages and current_messages[0].get("role") == "system":
                truncated_messages.append(current_messages[0])  # Keep system message
            
            # Add recent messages up to token limit
            remaining_tokens = model_total_context - 1000  # Reserve 1000 tokens for completion
            if truncated_messages:
                remaining_tokens -= self._count_tokens(self._convert_messages_to_prompt([truncated_messages[0]]))
            
            # Add messages from the end, working backwards
            for msg in reversed(current_messages[1:] if truncated_messages else current_messages):
                msg_tokens = self._count_tokens(f"{msg.get('role', '')}: {msg.get('content', '')}")
                if remaining_tokens - msg_tokens > 0:
                    truncated_messages.insert(-1 if len(truncated_messages) > 1 else len(truncated_messages), msg)
                    remaining_tokens -= msg_tokens
                else:
                    break
            
            current_messages = truncated_messages
            prompt = self._convert_messages_to_prompt(current_messages)
            num_prompt_tokens = self._count_tokens(prompt)
            max_completion_tokens = model_total_context - num_prompt_tokens
            
            print(f"✅ Truncated to {num_prompt_tokens} prompt tokens, {max_completion_tokens} available for completion")
        
        if max_completion_tokens <= 0:
            raise ValueError(
                f"Even after truncation, prompt is too long for Qwen model. "
                f"Prompt tokens: {num_prompt_tokens}, Model total context: {model_total_context}"
            )
        
        # Cap max tokens
        max_completion_tokens = min(max_completion_tokens, self.max_tokens)
        user_max_tokens = params_for_api.get('max_tokens')
        if user_max_tokens is not None:
            try:
                user_max_tokens = int(user_max_tokens)
                if user_max_tokens > 0:
                    max_completion_tokens = min(max_completion_tokens, user_max_tokens)
            except (ValueError, TypeError):
                pass
        
        # Ensure at least 1 token for completion
        if max_completion_tokens <= 0:
            max_completion_tokens = 1
        
        # Prepare API parameters
        api_params = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": max_completion_tokens,
            "temperature": params_for_api.get("temperature", self.temperature),
            "top_p": params_for_api.get("top_p", 1.0),
            "stop": params_for_api.get("stop", None),
        }
        
        # Remove None values
        api_params = {k: v for k, v in api_params.items() if v is not None}
        
        try:
            # Call the completions endpoint
            response = self.client.completions.create(**api_params)
            return self._convert_completions_response(response)
        except Exception as e:
            error_msg = str(e)
            if "maximum context length" in error_msg or "too many tokens" in error_msg:
                print(f"🚨 Token limit exceeded! Server error: {error_msg}")
                print(f"💡 Current settings: Context window={model_total_context}, Prompt tokens={num_prompt_tokens}")
                print(f"💡 Try setting: export QWEN_MAX_TOKENS=8192  # or your server's actual limit")
                raise RuntimeError(f"Token limit exceeded. Adjust QWEN_MAX_TOKENS environment variable. Error: {e}")
            else:
                raise RuntimeError(f"Error during Qwen API call: {e}")
    
    def _convert_messages_to_prompt(self, messages) -> str:
        """Convert ChatML messages format to a single prompt string."""
        prompt_parts = []
        
        for message in messages:
            role = message.get("role", "")
            content = message.get("content", "")
            
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"User: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
            else:
                prompt_parts.append(f"{role}: {content}")
        
        # Add assistant prompt to encourage a proper response
        prompt_parts.append("Assistant: Let me think about this step by step and provide a thoughtful response.\n\n")
        
        return "\n\n".join(prompt_parts)
    
    def _convert_completions_response(self, response):
        """Convert completions API response to chat completions format."""
        from datetime import datetime
        import uuid
        
        # Get the response data
        response_data = response.model_dump()
        
        # Extract the text from the completions response
        choice_data = response_data.get("choices", [{}])[0]
        text_content = choice_data.get("text", "")
        finish_reason = choice_data.get("finish_reason", "stop")
        
        # Extract usage information
        usage_data = response_data.get("usage", {})
        
        # Create a dictionary in ChatCompletion format
        chat_completion_dict = {
            "id": response_data.get("id", f"chatcmpl-{uuid.uuid4().hex}"),
            "object": "chat.completion",
            "created": response_data.get("created", int(datetime.now().timestamp())),
            "model": response_data.get("model", self.model_name),
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": text_content
                    },
                    "finish_reason": finish_reason
                }
            ],
            "usage": {
                "prompt_tokens": usage_data.get("prompt_tokens", 0),
                "completion_tokens": usage_data.get("completion_tokens", 0),
                "total_tokens": usage_data.get("total_tokens", 0)
            }
        }
        
        # Try to create a ChatCompletion object from the dictionary
        try:
            return ChatCompletion(**chat_completion_dict)
        except Exception as e:
            # If that fails, just return the original response
            print(f"Warning: Could not create ChatCompletion object: {e}")
            return response


class CodeLlamaModel(BaseModelBackend):
    r"""CodeLlama API model backend using completions endpoint.
    
    This backend is designed for locally hosted CodeLlama models served via vLLM
    with OpenAI-compatible API using the completions endpoint.
    
    Args:
        model_type (ModelType): The type of the model (should be ModelType.CODELLAMA_13B_INSTRUCT).
        model_config_dict (Dict): Configuration dictionary containing API settings
            like "api_key", "base_url", "temperature", etc.
    """

    def __init__(self, model_type: ModelType, model_config_dict: Dict[str, Any]) -> None:
        super().__init__(model_type, model_config_dict)
        
        # Debug: print what's in the config dict
        print(f"CodeLlamaModel config dict: {model_config_dict}")
        
        # Get API configuration
        self.api_key = self.model_config_dict.get("api_key") or os.getenv("OPENAI_API_KEY") or "fake-key"
        self.base_url = self.model_config_dict.get("base_url") or os.getenv("BASE_URL") or "http://localhost:12355/v1"
        
        # Make max_tokens configurable as hyperparameter
        self.model_max_tokens = int(os.getenv("CODELLAMA_MAX_TOKENS", "30208"))  # User-specified max tokens
        self.context_window = int(os.getenv("CODELLAMA_CONTEXT_WINDOW", str(self.model_max_tokens)))  # Total context window
        
        # Initialize OpenAI client with explicit parameter handling to avoid proxies issue
        try:
            # Try with base_url first
            import httpx
            http_client = httpx.Client()
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
                http_client=http_client
            )
        except Exception as e:
            print(f"Error with custom http client: {e}")
            try:
                # Try without custom http client
                self.client = openai.OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url
                )
            except Exception as e2:
                print(f"Error with base_url: {e2}")
                try:
                    # Last resort: minimal client without base_url
                    print("Falling back to minimal OpenAI client")
                    self.client = openai.OpenAI(
                        api_key=self.api_key
                    )
                    # Override base_url manually if needed
                    if self.base_url and hasattr(self.client, '_base_url'):
                        self.client._base_url = self.base_url
                except Exception as e3:
                    print(f"All OpenAI client initialization methods failed: {e3}")
                    raise RuntimeError(f"Cannot initialize OpenAI client: {e3}")
        
        self.model_name = self.model_config_dict.get("model", self.model_type.value)
        self.temperature = self.model_config_dict.get("temperature", 0.1)  # Lower temperature for code generation
        self.max_tokens = self.model_config_dict.get("max_tokens") or min(4096, self.model_max_tokens // 4)  # Default to 1/4 of context for completion
        
        # Initialize CodeLlama tokenizer (fallback to tiktoken if not available)
        try:
            from transformers import AutoTokenizer
            # Use CodeLlama tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-hf", trust_remote_code=True)
            self.use_codellama_tokenizer = True
            print("✅ Loaded CodeLlama tokenizer successfully")
        except Exception as e:
            print(f"⚠️  Could not load CodeLlama tokenizer ({e}), falling back to tiktoken approximation")
            self.tokenizer = None
            self.use_codellama_tokenizer = False

    def _count_tokens(self, text: str) -> int:
        """Count tokens using CodeLlama tokenizer or fallback to tiktoken."""
        if self.use_codellama_tokenizer and self.tokenizer:
            # Use the proper CodeLlama tokenizer
            return len(self.tokenizer.encode(text))
        else:
            # Fallback to tiktoken approximation
            try:
                encoding = tiktoken.encoding_for_model(self.model_type.value_for_tiktoken)
            except KeyError:
                encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))

    def run(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """Run the CodeLlama model using completions API."""
        
        params_for_api = kwargs.copy()
        current_messages = params_for_api.pop("messages", None)
        
        if not current_messages:
            raise ValueError("Messages not found in parameters for CodeLlamaModel.run")
        
        # Convert messages array to a single prompt string
        prompt = self._convert_messages_to_prompt(current_messages)
        
        # Calculate token limits using proper CodeLlama tokenizer
        num_prompt_tokens = self._count_tokens(prompt)
        
        # Set token limits for CodeLlama model (use actual server limit)
        model_total_context = self.context_window # Use the configurable context window
        max_completion_tokens = model_total_context - num_prompt_tokens
        
        # If prompt is too long, truncate messages
        if max_completion_tokens <= 100:  # Need at least 100 tokens for completion
            print(f"⚠️  Prompt too long ({num_prompt_tokens} tokens), truncating messages...")
            print(f"   Model context window: {model_total_context}, Prompt tokens: {num_prompt_tokens}")
            
            # Keep system message and recent messages
            truncated_messages = []
            if current_messages and current_messages[0].get("role") == "system":
                truncated_messages.append(current_messages[0])  # Keep system message
            
            # Add recent messages up to token limit
            remaining_tokens = model_total_context - 1000  # Reserve 1000 tokens for completion
            if truncated_messages:
                remaining_tokens -= self._count_tokens(self._convert_messages_to_prompt([truncated_messages[0]]))
            
            # Add messages from the end, working backwards
            for msg in reversed(current_messages[1:] if truncated_messages else current_messages):
                msg_tokens = self._count_tokens(f"{msg.get('role', '')}: {msg.get('content', '')}")
                if remaining_tokens - msg_tokens > 0:
                    truncated_messages.insert(-1 if len(truncated_messages) > 1 else len(truncated_messages), msg)
                    remaining_tokens -= msg_tokens
                else:
                    break
            
            current_messages = truncated_messages
            prompt = self._convert_messages_to_prompt(current_messages)
            num_prompt_tokens = self._count_tokens(prompt)
            max_completion_tokens = model_total_context - num_prompt_tokens
            
            print(f"✅ Truncated to {num_prompt_tokens} prompt tokens, {max_completion_tokens} available for completion")
        
        if max_completion_tokens <= 0:
            raise ValueError(
                f"Even after truncation, prompt is too long for CodeLlama model. "
                f"Prompt tokens: {num_prompt_tokens}, Model total context: {model_total_context}"
            )
        
        # Cap max tokens
        max_completion_tokens = min(max_completion_tokens, self.max_tokens)
        user_max_tokens = params_for_api.get('max_tokens')
        if user_max_tokens is not None:
            try:
                user_max_tokens = int(user_max_tokens)
                if user_max_tokens > 0:
                    max_completion_tokens = min(max_completion_tokens, user_max_tokens)
            except (ValueError, TypeError):
                pass
        
        # Ensure at least 1 token for completion
        if max_completion_tokens <= 0:
            max_completion_tokens = 1
        
        # Prepare API parameters
        api_params = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": max_completion_tokens,
            "temperature": params_for_api.get("temperature", self.temperature),
            "top_p": params_for_api.get("top_p", 1.0),
            "stop": params_for_api.get("stop", None),
        }
        
        # Remove None values
        api_params = {k: v for k, v in api_params.items() if v is not None}
        
        try:
            # Call the completions endpoint
            response = self.client.completions.create(**api_params)
            return self._convert_completions_response(response)
        except Exception as e:
            error_msg = str(e)
            if "maximum context length" in error_msg or "too many tokens" in error_msg:
                print(f"🚨 Token limit exceeded! Server error: {error_msg}")
                print(f"💡 Current settings: Context window={model_total_context}, Prompt tokens={num_prompt_tokens}")
                print(f"💡 Try setting: export CODELLAMA_MAX_TOKENS=8192  # or your server's actual limit")
                raise RuntimeError(f"Token limit exceeded. Adjust CODELLAMA_MAX_TOKENS environment variable. Error: {e}")
            else:
                raise RuntimeError(f"Error during CodeLlama API call: {e}")
    
    def _convert_messages_to_prompt(self, messages) -> str:
        """Convert ChatML messages format to a single prompt string optimized for CodeLlama."""
        prompt_parts = []
        
        for message in messages:
            role = message.get("role", "")
            content = message.get("content", "")
            
            if role == "system":
                prompt_parts.append(f"[INST] System: {content} [/INST]")
            elif role == "user":
                prompt_parts.append(f"[INST] {content} [/INST]")
            elif role == "assistant":
                prompt_parts.append(f"{content}")
            else:
                prompt_parts.append(f"[INST] {role}: {content} [/INST]")
        
        # For CodeLlama, use its instruction format
        return "\n\n".join(prompt_parts) + "\n\n"
    
    def _convert_completions_response(self, response):
        """Convert completions API response to chat completions format."""
        from datetime import datetime
        import uuid
        
        # Get the response data
        response_data = response.model_dump()
        
        # Extract the text from the completions response
        choice_data = response_data.get("choices", [{}])[0]
        text_content = choice_data.get("text", "")
        finish_reason = choice_data.get("finish_reason", "stop")
        
        # Extract usage information
        usage_data = response_data.get("usage", {})
        
        # Create a dictionary in ChatCompletion format
        chat_completion_dict = {
            "id": response_data.get("id", f"chatcmpl-{uuid.uuid4().hex}"),
            "object": "chat.completion",
            "created": response_data.get("created", int(datetime.now().timestamp())),
            "model": response_data.get("model", self.model_name),
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": text_content
                    },
                    "finish_reason": finish_reason
                }
            ],
            "usage": {
                "prompt_tokens": usage_data.get("prompt_tokens", 0),
                "completion_tokens": usage_data.get("completion_tokens", 0),
                "total_tokens": usage_data.get("total_tokens", 0)
            }
        }
        
        # Try to create a ChatCompletion object from the dictionary
        try:
            return ChatCompletion(**chat_completion_dict)
        except Exception as e:
            # If that fails, just return the original response
            print(f"Warning: Could not create ChatCompletion object: {e}")
            return response


class ModelFactory:
    r"""Factory of backend models.

    Raises:
        ValueError: in case the provided model type is unknown.
    """

    @staticmethod
    def create(model_type: ModelType, model_config_dict: Dict) -> BaseModelBackend: # Changed to BaseModelBackend
        # Determine the effective model_type to use, defaulting if None is provided.
        # This default_model_type is crucial if model_type can be None.
        # However, model_type in ChatChain is usually resolved before this factory.
        effective_model_type = model_type if model_type is not None else ModelType.GPT_3_5_TURBO

        if effective_model_type in {
            ModelType.GPT_3_5_TURBO,
            ModelType.GPT_3_5_TURBO_NEW, # Ensure this is handled or aliased if it's the same as GPT_3_5_TURBO
            ModelType.GPT_3_5_TURBO_16K,
            ModelType.GPT_4,
            ModelType.GPT_4_32k, # Note: Using lowercase k to match the enum definition
            ModelType.GPT_4_TURBO,
            ModelType.GPT_4_TURBO_V, # Ensure this is handled or aliased
            ModelType.GPT_4_TURBO_PREVIEW,
            ModelType.GPT_4_VISION_PREVIEW,
            ModelType.GPT_4O,
            ModelType.GPT_4O_MINI,
            ModelType.GPT_45, # Ensure this is handled
        }:
            model_class = OpenAIModel
        elif effective_model_type == ModelType.STUB:
            model_class = StubModel
        elif effective_model_type == ModelType.CLAUDE:
            model_class = ClaudeModel
        elif effective_model_type == ModelType.QWEN_2_5_CODER_32B:
            model_class = QwenModel
        elif effective_model_type == ModelType.CODELLAMA_13B_INSTRUCT:
            model_class = CodeLlamaModel
        else:
            # If the original model_type was None and default_model_type was, for example, CLAUDE,
            # this logic needs to correctly pick it up.
            # The current structure with effective_model_type should handle this.
            raise ValueError(f"Unknown or unsupported model type: {effective_model_type}")

        # log_visualize("Model Type: {}".format(effective_model_type))
        # Pass the original model_type (if specified) or the resolved default_model_type
        # to the constructor. The class itself knows how to handle its specific type.
        inst = model_class(effective_model_type, model_config_dict)
        return inst
