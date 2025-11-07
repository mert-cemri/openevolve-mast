#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/12/19 14:00
@Author  : mert
@File    : codellama_api.py
@Desc    : CodeLlama LLM provider for MetaGPT
"""
import json
import os
from typing import Any, Dict, List, Optional, Union

import openai
from metagpt.configs.llm_config import LLMConfig, LLMType
from metagpt.const import USE_CONFIG_TIMEOUT
from metagpt.logs import logger
from metagpt.provider.base_llm import BaseLLM
from metagpt.provider.llm_provider_registry import register_provider


@register_provider(LLMType.CODELLAMA)
class CodeLlamaLLM(BaseLLM):
    """CodeLlama LLM provider using OpenAI-compatible completions API"""

    def __init__(self, config: LLMConfig):
        self.config = config
        self.model = config.model or "CodeLlama-13b-Instruct"
        self.temperature = getattr(config, 'temperature', 0.7)
        
        # Set up the OpenAI client for CodeLlama vLLM server
        base_url = config.base_url or os.getenv("BASE_URL", "http://localhost:12355/v1")
        api_key = config.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
        
        self.client = openai.AsyncOpenAI(
            base_url=base_url,
            api_key=api_key,
            timeout=120.0,  # Increased timeout for CodeLlama 13B model
        )
        
        # Initialize tokenizer for accurate token counting
        self.tokenizer = None
        self.use_codellama_tokenizer = False
        try:
            from transformers import AutoTokenizer
            # Use CodeLlama tokenizer for accurate token counting
            # Map served model name to HuggingFace model identifier
            model_mapping = {
                "CodeLlama-13b-Instruct": "codellama/CodeLlama-13b-Instruct-hf",
                "codellama/CodeLlama-13b-Instruct-hf": "codellama/CodeLlama-13b-Instruct-hf"
            }
            tokenizer_model = model_mapping.get(self.model, "codellama/CodeLlama-13b-Instruct-hf")
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_model, trust_remote_code=True)
            self.use_codellama_tokenizer = True
            logger.info(f"✅ Loaded CodeLlama tokenizer successfully for {tokenizer_model}")
        except Exception as e:
            logger.warning(f"⚠️  Could not load CodeLlama tokenizer ({e}), falling back to tiktoken approximation")
            try:
                import tiktoken
                self.fallback_tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")
            except:
                self.fallback_tokenizer = None

    def _convert_messages_to_prompt(self, messages: List[Dict[str, str]]) -> str:
        """Convert messages array to a single prompt string for CodeLlama"""
        prompt_parts = []
        
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")
            
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"User: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
        
        # Add assistant prompt to encourage response
        if not prompt_parts or not prompt_parts[-1].startswith("Assistant:"):
            prompt_parts.append("Assistant:")
        
        return "\n\n".join(prompt_parts)

    def _count_tokens(self, text: str) -> int:
        """Count tokens using CodeLlama tokenizer or fallback"""
        if self.use_codellama_tokenizer and self.tokenizer:
            try:
                tokens = self.tokenizer.encode(text)
                return len(tokens)
            except Exception as e:
                logger.warning(f"CodeLlama tokenizer failed: {e}")
        
        # Fallback to tiktoken approximation
        if hasattr(self, 'fallback_tokenizer') and self.fallback_tokenizer:
            try:
                return len(self.fallback_tokenizer.encode(text))
            except:
                pass
        
        # Final fallback - rough approximation
        return len(text) // 4

    async def _achat_completion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        """Main chat completion method"""
        
        # Convert messages to prompt format for CodeLlama
        prompt = self._convert_messages_to_prompt(messages)
        
        # Calculate token limits
        prompt_tokens = self._count_tokens(prompt)
        max_context_tokens = 30208  # CodeLlama context window
        max_completion_tokens = min(
            kwargs.get('max_tokens', 2048),
            max_context_tokens - prompt_tokens - 100  # Safety buffer
        )
        
        if max_completion_tokens <= 0:
            raise ValueError(f"Prompt too long: {prompt_tokens} tokens exceeds context limit")
        
        temperature = kwargs.get('temperature', self.temperature)
        
        logger.info(f"🦙 CodeLlama API call - Model: {self.model}, Prompt tokens: {prompt_tokens}, Max completion: {max_completion_tokens}")
        
        try:
            # Use non-streaming completions endpoint with retries for CodeLlama
            import asyncio
            
            for attempt in range(3):  # Try up to 3 times
                try:
                    response = await self.client.completions.create(
                        model=self.model,
                        prompt=prompt,
                        max_tokens=max_completion_tokens,
                        temperature=temperature,
                        stream=False
                    )
                    break  # Success, exit retry loop
                except Exception as e:
                    if attempt == 2:  # Last attempt
                        raise e
                    logger.warning(f"CodeLlama API attempt {attempt + 1}/3 failed: {e}. Retrying in 5s...")
                    await asyncio.sleep(5)
            
            # Extract the generated text
            if response.choices and len(response.choices) > 0:
                generated_text = response.choices[0].text.strip()
                logger.info(f"✅ CodeLlama response received: {len(generated_text)} characters")
                
                # Convert to chat completion format for compatibility
                return {
                    "choices": [{
                        "message": {
                            "role": "assistant",
                            "content": generated_text
                        },
                        "finish_reason": response.choices[0].finish_reason
                    }],
                    "usage": {
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": self._count_tokens(generated_text),
                        "total_tokens": prompt_tokens + self._count_tokens(generated_text)
                    },
                    "model": self.model
                }
            else:
                raise ValueError("No response choices returned from CodeLlama API")
                
        except Exception as e:
            logger.error(f"CodeLlama API call failed: {e}")
            raise

    async def acompletion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        """Wrapper for completion method"""
        return await self._achat_completion(messages, **kwargs)

    def completion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        """Synchronous completion method"""
        import asyncio
        return asyncio.run(self._achat_completion(messages, **kwargs))

    async def aask(
        self,
        msg: Union[str, List[Dict[str, str]]],
        system_msgs: Optional[List[str]] = None,
        format_msgs: Optional[List[Dict[str, str]]] = None,
        images: Optional[Union[str, List[str]]] = None,
        timeout: int = 60,
        stream: bool = None,
        **kwargs
    ) -> str:
        """Ask method that matches MetaGPT's expected signature"""
        messages = []
        
        # Add system messages if provided
        if system_msgs:
            for sys_msg in system_msgs:
                messages.append({"role": "system", "content": sys_msg})
        
        # Add format messages if provided
        if format_msgs:
            messages.extend(format_msgs)
        
        # Add user message
        if isinstance(msg, str):
            messages.append({"role": "user", "content": msg})
        elif isinstance(msg, list):
            # If msg is already a list of messages, extend it
            messages.extend(msg)
        
        response = await self._achat_completion(messages, **kwargs)
        return response["choices"][0]["message"]["content"]

    def ask(self, msg: str, system_msgs: Optional[List[str]] = None, **kwargs) -> str:
        """Synchronous ask method"""
        import asyncio
        return asyncio.run(self.aask(msg, system_msgs, **kwargs))

    @property
    def use_system_prompt(self) -> bool:
        """CodeLlama supports system prompts"""
        return True

    def get_choice_text(self, resp: Dict[str, Any]) -> str:
        """Extract text from response"""
        return resp["choices"][0]["message"]["content"]

    def get_choice_function(self, resp: Dict[str, Any]) -> Dict[str, Any]:
        """CodeLlama doesn't support function calling"""
        return {}

    async def _achat_completion_stream(self, messages: List[Dict[str, str]], **kwargs):
        """Streaming completion method - not implemented for CodeLlama"""
        # For now, we'll just call the non-streaming version and yield the complete response
        response = await self._achat_completion(messages, **kwargs)
        yield response 