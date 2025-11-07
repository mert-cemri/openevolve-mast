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
from enum import Enum
from typing import Dict, List, Optional, Union
from pydantic import BaseModel


class TaskType(Enum):
    AI_SOCIETY = "ai_society"
    CODE = "code"
    MISALIGNMENT = "misalignment"
    TRANSLATION = "translation"
    EVALUATION = "evaluation"
    SOLUTION_EXTRACTION = "solution_extraction"
    CHATDEV = "chat_dev"
    DEFAULT = "default"


class RoleType(str, Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    CRITIC = "critic"
    EMBODIMENT = "embodiment"
    DEFAULT = "default"
    CHATDEV = "AgentTech"
    CHATDEV_COUNSELOR = "counselor"
    CHATDEV_CEO = "chief executive officer (CEO)"
    CHATDEV_CHRO = "chief human resource officer (CHRO)"
    CHATDEV_CPO = "chief product officer (CPO)"
    CHATDEV_CTO = "chief technology officer (CTO)"
    CHATDEV_PROGRAMMER = "programmer"
    CHATDEV_REVIEWER = "code reviewer"
    CHATDEV_TESTER = "software test engineer"
    CHATDEV_CCO = "chief creative officer (CCO)"


class ModelType(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_NEW = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_4 = "gpt-4"
    GPT_4_32k = "gpt-4-32k"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4_TURBO_V = "gpt-4-turbo"
    GPT_4_TURBO_PREVIEW = "gpt-4-turbo-preview"
    GPT_4_VISION_PREVIEW = "gpt-4-vision-preview"
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_45 = "gpt-4.5-preview"
    STUB = "stub"
    CLAUDE = "claude"
    QWEN_2_5_CODER_32B = "Qwen2.5-Coder-32B-Instruct"
    CODELLAMA_13B_INSTRUCT = "CodeLlama-13b-Instruct"

    @property
    def value_for_tiktoken(self):
        if self.name == "STUB":
            return "gpt-3.5-turbo-16k-0613"
        elif self.name in ["QWEN_2_5_CODER_32B", "CODELLAMA_13B_INSTRUCT"]:
            # Use GPT-4 as fallback for non-OpenAI models that tiktoken doesn't know about
            return "gpt-4"
        else:
            return self.value


class PhaseType(Enum):
    REFLECTION = "reflection"
    RECRUITING_CHRO = "recruiting CHRO"
    RECRUITING_CPO = "recruiting CPO"
    RECRUITING_CTO = "recruiting CTO"
    DEMAND_ANALYSIS = "demand analysis"
    CHOOSING_LANGUAGE = "choosing language"
    RECRUITING_PROGRAMMER = "recruiting programmer"
    RECRUITING_REVIEWER = "recruiting reviewer"
    RECRUITING_TESTER = "recruiting software test engineer"
    RECRUITING_CCO = "recruiting chief creative officer"
    CODING = "coding"
    CODING_COMPLETION = "coding completion"
    CODING_AUTOMODE = "coding auto mode"
    REVIEWING_COMMENT = "review comment"
    REVIEWING_MODIFICATION = "code modification after reviewing"
    ERROR_SUMMARY = "error summary"
    MODIFICATION = "code modification"
    ART_ELEMENT_ABSTRACTION = "art element abstraction"
    ART_ELEMENT_INTEGRATION = "art element integration"
    CREATING_ENVIRONMENT_DOCUMENT = "environment document"
    CREATING_USER_MANUAL = "user manual"


class ChatMessage(BaseModel):
    role: str
    content: str


class Choice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: Optional[str] = None


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ModelResponse(BaseModel):
    id: str
    model: ModelType
    choices: List[Choice]
    usage: Usage


__all__ = ["TaskType", "RoleType", "ModelType", "PhaseType"]
