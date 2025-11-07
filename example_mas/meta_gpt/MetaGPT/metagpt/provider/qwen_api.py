#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/12/19 12:00
@Author  : mert
@File    : qwen_api.py
@Desc    : Qwen LLM provider for MetaGPT, adapted from ChatDev QwenModel
"""
import json
import os
from typing import Any, Dict, List, Optional

import openai
from metagpt.configs.llm_config import LLMConfig, LLMType
from metagpt.const import USE_CONFIG_TIMEOUT
from metagpt.logs import logger
from metagpt.provider.base_llm import BaseLLM
from metagpt.provider.llm_provider_registry import register_provider


@register_provider(LLMType.QWEN)
class QwenLLM(BaseLLM):
    """Qwen LLM provider using OpenAI-compatible completions API"""

    def __init__(self, config: LLMConfig):
        self.config = config
        self.model = config.model or "Qwen2.5-Coder-32B-Instruct"
        
        # Get API configuration from config or environment
        api_key = config.api_key or os.getenv("OPENAI_API_KEY", "fake-key")
        base_url = config.base_url or os.getenv("BASE_URL", "http://localhost:12355/v1")
        
        # Initialize OpenAI client for Qwen API
        self.client = openai.AsyncOpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        # Model configuration
        self.temperature = config.temperature
        self.max_tokens = config.max_token or 4096
        self.use_system_prompt = config.use_system_prompt
        
        # Initialize tokenizer for accurate token counting
        self.tokenizer = None
        self.use_qwen_tokenizer = False
        try:
            from transformers import AutoTokenizer
            # Use the same model for tokenizer as the actual model being used
            tokenizer_model = self.model or "Qwen/Qwen2.5-Coder-32B-Instruct"
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_model, trust_remote_code=True)
            self.use_qwen_tokenizer = True
            logger.info(f"✅ Loaded Qwen tokenizer successfully for {tokenizer_model}")
        except Exception as e:
            logger.warning(f"⚠️  Could not load Qwen tokenizer ({e}), falling back to tiktoken approximation")

    def _count_tokens(self, text: str) -> int:
        """Count tokens using Qwen tokenizer or fallback to tiktoken."""
        if self.use_qwen_tokenizer and self.tokenizer:
            return len(self.tokenizer.encode(text))
        else:
            # Fallback to tiktoken approximation
            try:
                import tiktoken
                encoding = tiktoken.get_encoding("cl100k_base")
                return len(encoding.encode(text))
            except Exception:
                # Last resort: rough estimation (1 token ≈ 4 characters)
                return len(text) // 4

    def _convert_messages_to_prompt(self, messages: List[dict]) -> str:
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
        prompt_parts.append("Assistant:")
        
        return "\n\n".join(prompt_parts)

    async def _achat_completion(self, messages: List[dict], timeout=USE_CONFIG_TIMEOUT):
        """Async chat completion using Qwen completions API"""
        # Convert messages to prompt
        prompt = self._convert_messages_to_prompt(messages)
        
        # Calculate token limits
        num_prompt_tokens = self._count_tokens(prompt)
        context_window = int(os.getenv("QWEN_CONTEXT_WINDOW", "30208"))
        max_completion_tokens = min(self.max_tokens, context_window - num_prompt_tokens - 100)
        
        if max_completion_tokens <= 0:
            raise ValueError(f"Prompt too long: {num_prompt_tokens} tokens, max context: {context_window}")
        
        try:
            # Call the completions endpoint
            response = await self.client.completions.create(
                model=self.model,
                prompt=prompt,
                max_tokens=max_completion_tokens,
                temperature=self.temperature,
                stream=False
            )
            
            # Convert completions response to chat completion format
            choice_text = response.choices[0].text.strip()
            
            # Update costs if available
            if hasattr(response, 'usage') and response.usage:
                self._update_costs(response.usage.model_dump(), self.model)
            
            return {
                "choices": [{
                    "message": {
                        "role": "assistant",
                        "content": choice_text
                    }
                }],
                "usage": response.usage.model_dump() if hasattr(response, 'usage') else {}
            }
            
        except Exception as e:
            logger.error(f"Qwen API call failed: {e}")
            raise

    async def acompletion(self, messages: List[dict], timeout=USE_CONFIG_TIMEOUT):
        """Async completion interface"""
        return await self._achat_completion(messages, timeout)

    async def _achat_completion_stream(self, messages: List[dict], timeout: int = USE_CONFIG_TIMEOUT) -> str:
        """Async streaming completion"""
        # Convert messages to prompt
        prompt = self._convert_messages_to_prompt(messages)
        
        # Calculate token limits
        num_prompt_tokens = self._count_tokens(prompt)
        context_window = int(os.getenv("QWEN_CONTEXT_WINDOW", "30208"))
        max_completion_tokens = min(self.max_tokens, context_window - num_prompt_tokens - 100)
        
        if max_completion_tokens <= 0:
            raise ValueError(f"Prompt too long: {num_prompt_tokens} tokens, max context: {context_window}")
        
        try:
            # Use non-streaming for now to avoid pydantic validation issues
            response = await self.client.completions.create(
                model=self.model,
                prompt=prompt,
                max_tokens=max_completion_tokens,
                temperature=self.temperature,
                stream=False
            )
            
            # Extract text from response
            collected_content = response.choices[0].text.strip()
            
            # Print content to simulate streaming
            print(collected_content, end="", flush=True)
            
            return collected_content
            
        except Exception as e:
            logger.error(f"Qwen API call failed: {e}")
            raise 