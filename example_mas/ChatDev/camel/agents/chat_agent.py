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
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from tenacity import retry, retry_if_exception_type
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_exponential

from camel.agents import BaseAgent
from camel.configs import ChatGPTConfig
from camel.messages import ChatMessage, MessageType, SystemMessage
from camel.model_backend import BaseModelBackend as ModelBackend, ModelFactory
from camel.typing import ModelType, RoleType
from camel.utils import (
    get_model_token_limit,
    num_tokens_from_messages,
    openai_api_key_required,
)
from chatdev.utils import log_visualize

# Define retry constants
RETRY_TIMES = 6
MIN_WAIT_TIME = 1
MAX_WAIT_TIME = 60

try:
    from openai.types.chat import ChatCompletion

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version


@dataclass(frozen=True)
class ChatAgentResponse:
    r"""Response of a ChatAgent.

    Attributes:
        msgs (List[ChatMessage]): A list of zero, one or several messages.
            If the list is empty, there is some error in message generation.
            If the list has one message, this is normal mode.
            If the list has several messages, this is the critic mode.
        terminated (bool): A boolean indicating whether the agent decided
            to terminate the chat session.
        info (Dict[str, Any]): Extra information about the chat message.
    """
    msgs: List[ChatMessage]
    terminated: bool
    info: Dict[str, Any]

    @property
    def msg(self):
        if self.terminated:
            raise RuntimeError("error in ChatAgentResponse, info:{}".format(str(self.info)))
        if len(self.msgs) > 1:
            raise RuntimeError("Property msg is only available for a single message in msgs")
        elif len(self.msgs) == 0:
            if len(self.info) > 0:
                raise RuntimeError("Empty msgs in ChatAgentResponse, info:{}".format(str(self.info)))
            else:
                # raise RuntimeError("Known issue that msgs is empty and there is no error info, to be fix")
                return None
        return self.msgs[0]


class ChatAgent(BaseAgent):
    r"""Class for managing conversations of CAMEL Chat Agents.

    Args:
        system_message (SystemMessage): The system message for the chat agent.
        with_memory(bool): The memory setting of the chat agent.
        model (ModelType, optional): The LLM model to use for generating
            responses. (default :obj:`ModelType.GPT_3_5_TURBO`)
        model_config (Any, optional): Configuration options for the LLM model.
            (default: :obj:`None`)
        message_window_size (int, optional): The maximum number of previous
            messages to include in the context window. If `None`, no windowing
            is performed. (default: :obj:`None`)
    """

    def __init__(
            self,
            system_message: SystemMessage,
            memory = None,
            model: Optional[ModelType] = None,
            model_config: Optional[Any] = None,
            message_window_size: Optional[int] = None,
    ) -> None:

        self.system_message: SystemMessage = system_message
        self.role_name: str = system_message.role_name
        self.role_type: RoleType = system_message.role_type
        self.model: ModelType = (model if model is not None else ModelType.GPT_3_5_TURBO)
        self.model_config: ChatGPTConfig = model_config or ChatGPTConfig()
        self.model_token_limit: int = get_model_token_limit(self.model)
        self.message_window_size: Optional[int] = message_window_size
        self.model_backend: ModelBackend = ModelFactory.create(self.model, self.model_config.__dict__)
        self.terminated: bool = False
        self.info: bool = False
        self.init_messages()
        if memory !=None and self.role_name in["Code Reviewer","Programmer","Software Test Engineer"]:
            self.memory = memory.memory_data.get("All")
        else:
            self.memory = None

    def reset(self) -> List[MessageType]:
        r"""Resets the :obj:`ChatAgent` to its initial state and returns the
        stored messages.

        Returns:
            List[MessageType]: The stored messages.
        """
        self.terminated = False
        self.init_messages()
        return self.stored_messages

    def get_info(
            self,
            id: Optional[str],
            usage: Optional[Dict[str, int]],
            termination_reasons: List[str],
            num_tokens: int,
    ) -> Dict[str, Any]:
        r"""Returns a dictionary containing information about the chat session.

        Args:
            id (str, optional): The ID of the chat session.
            usage (Dict[str, int], optional): Information about the usage of
                the LLM model.
            termination_reasons (List[str]): The reasons for the termination of
                the chat session.
            num_tokens (int): The number of tokens used in the chat session.

        Returns:
            Dict[str, Any]: The chat session information.
        """
        return {
            "id": id,
            "usage": usage,
            "termination_reasons": termination_reasons,
            "num_tokens": num_tokens,
        }

    def init_messages(self) -> None:
        r"""Initializes the stored messages list with the initial system
        message.
        """
        self.stored_messages: List[MessageType] = [self.system_message]

    def update_messages(self, message: ChatMessage) -> List[MessageType]:
        r"""Updates the stored messages list with a new message.

        Args:
            message (ChatMessage): The new message to add to the stored
                messages.

        Returns:
            List[ChatMessage]: The updated stored messages.
        """
        self.stored_messages.append(message)
        return self.stored_messages
    def use_memory(self,input_message) -> List[MessageType]:
        if self.memory is None :
            return None
        else:
            if self.role_name == "Programmer":
                result = self.memory.memory_retrieval(input_message,"code")
                if result != None:
                    target_memory,distances, mids,task_list,task_dir_list = result
                    if target_memory != None and len(target_memory) != 0:
                        target_memory="".join(target_memory)
                        #self.stored_messages[-1].content = self.stored_messages[-1].content+"Here is some code you've previously completed:"+target_memory+"You can refer to the previous script to complement this task."
                        log_visualize(self.role_name,
                                            "thinking back and found some related code: \n--------------------------\n"
                                            + target_memory)
                else:
                    target_memory = None
                    log_visualize(self.role_name,
                                         "thinking back but find nothing useful")

            else:
                result = self.memory.memory_retrieval(input_message, "text")
                if result != None:
                    target_memory, distances, mids, task_list, task_dir_list = result
                    if target_memory != None and len(target_memory) != 0:
                        target_memory=";".join(target_memory)
                        #self.stored_messages[-1].content = self.stored_messages[-1].content+"Here are some effective and efficient instructions you have sent to the assistant :"+target_memory+"You can refer to these previous excellent instructions to better instruct assistant here."
                        log_visualize(self.role_name,
                                            "thinking back and found some related text: \n--------------------------\n"
                                            + target_memory)
                else:
                    target_memory = None
                    log_visualize(self.role_name,
                                         "thinking back but find nothing useful")

        return target_memory

    @retry(stop=stop_after_attempt(RETRY_TIMES),
           wait=wait_exponential(min=MIN_WAIT_TIME,
                                 max=MAX_WAIT_TIME),
           retry=retry_if_exception_type(RuntimeError))
    @openai_api_key_required
    def step(
            self,
            input_message: Optional[ChatMessage] = None,
    ) -> ChatAgentResponse:
        r"""Performs one step of the conversation.

        Args:
            input_message (ChatMessage, optional): An optional input message to
                process. (default: :obj:`None`)

        Returns:
            ChatAgentResponse: The chat agent's response.
        """
        if input_message:
            self.update_messages(input_message)

        # Use memory if available
        memory_messages = self.use_memory(input_message)
        send_messages = self.stored_messages
        if memory_messages is not None:
            # print("using memory")
            send_messages = self.stored_messages + memory_messages

        num_tokens = num_tokens_from_messages(
            [message.to_openai_message() for message in send_messages],
            self.model,
        )

        if self.message_window_size:
            original_tokens = num_tokens
            # Window stored messages to fit within token limit.
            # Always keep the system message.
            system_message, user_messages = self.stored_messages[0], self.stored_messages[1:]
            windowed_messages = [system_message]
            if memory_messages is not None:
                user_messages = user_messages + memory_messages
            # Introduce a variable to record current number of tokens consumed.
            # Note that we count the token number based on stored_messages
            # instead of user_messages. After windowing, we still need to update
            # stored_messages for next round.
            curr_tokens = num_tokens_from_messages(
                [system_message.to_openai_message()], self.model
            )

            for message in reversed(user_messages):
                num_message_tokens = num_tokens_from_messages(
                    [message.to_openai_message()], self.model
                )
                # Add tokens for this message. If it exceeds the limit,
                # stop adding messages.
                if (curr_tokens + num_message_tokens) > self.model_token_limit:
                    if num_message_tokens > self.model_token_limit:
                        # Edge case: a single message exceeds the token limit.
                        # In this case, let's continue but the message will be
                        # truncated by the model.
                        pass
                    else:
                        continue
                curr_tokens += num_message_tokens
                windowed_messages.insert(1, message)

            if memory_messages is not None:
                num_memory_messages = len(memory_messages)
                windowed_messages = windowed_messages[:-num_memory_messages]
                # log_visualize(f"Number of token reduced from {original_tokens} to {curr_tokens} after windowing")
                # log_visualize(f"\n\n {windowed_messages} after windowing")

            messages_to_send = [
                message.to_openai_message() for message in windowed_messages
            ]
        else:
            messages_to_send = [
                message.to_openai_message() for message in send_messages
            ]

        content = None
        success = False
        termination_reasons = []

        # Create a copy of model_config_dict and ensure it's mutable
        model_config_dict = dict(self.model_config.__dict__)
        
        # Prepare model parameters
        response = self.model_backend.run(messages=messages_to_send, **model_config_dict)

        # Handle different response structures based on model type
        if self.model == ModelType.CLAUDE:
            # Handle Claude API response format
            try:
                choices = response.get("choices", [])
                if not choices or len(choices) == 0:
                    raise RuntimeError("Claude API returned empty choices")
                    
                content = choices[0]["message"]["content"]
                role = choices[0]["message"]["role"]
                
                if role != "assistant":
                    raise RuntimeError(f"Expected role 'assistant', got '{role}'")
                    
                finish_reason = choices[0].get("finish_reason", "stop")
                termination_reasons.append(finish_reason)
                success = True
                
                usage = response.get("usage", {})
                prompt_tokens = usage.get("prompt_tokens", 0)
                completion_tokens = usage.get("completion_tokens", 0)
                total_tokens = usage.get("total_tokens", 0)
                
            except Exception as e:
                raise RuntimeError(f"Claude returned unexpected struct: {str(e)}")
            
        elif openai_new_api:
            # Handle the new OpenAI API response format
            try:
                if not isinstance(response, ChatCompletion):
                    raise RuntimeError("Response is not a valid ChatCompletion object")
                    
                if not response.choices:
                    raise RuntimeError("No choices in model response")
                    
                content = response.choices[0].message.content
                finish_reason = response.choices[0].finish_reason
                termination_reasons.append(finish_reason)
                success = True
                
                prompt_tokens = response.usage.prompt_tokens
                completion_tokens = response.usage.completion_tokens
                total_tokens = response.usage.total_tokens
                
            except Exception as e:
                raise RuntimeError(f"OpenAI returned unexpected struct: {str(e)}")
        else:
            # Handle the old OpenAI API response format
            if "error" in response:
                raise RuntimeError(response["error"])
            
            if "choices" not in response or len(response["choices"]) == 0:
                raise RuntimeError("OpenAI returned unexpected struct")
            
            content = response["choices"][0]["message"]["content"]
            finish_reason = response["choices"][0]["finish_reason"]
            termination_reasons.append(finish_reason)
            success = True
            
            prompt_tokens = response["usage"]["prompt_tokens"]
            completion_tokens = response["usage"]["completion_tokens"]
            total_tokens = response["usage"]["total_tokens"]

        if not success or not content:
            if len(termination_reasons) > 0:
                return ChatAgentResponse(
                    msgs=[],
                    terminated=True,
                    info=self.get_info(
                        id=None,
                        usage=None,
                        termination_reasons=termination_reasons,
                        num_tokens=num_tokens,
                    ),
                )
            else:
                raise RuntimeError("Model call failed for unknown reason")

        # Check for terminate signal to end the dialog
        if "TERMINATE" in content:
            return ChatAgentResponse(
                msgs=[],
                terminated=True,
                info=self.get_info(
                    id=getattr(response, "id", None),
                    usage={
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": total_tokens,
                    },
                    termination_reasons=termination_reasons,
                    num_tokens=num_tokens,
                ),
            )

        # Return a normal response
        critique_messages = []
        start_idx = content.find("<!--")
        if start_idx != -1:
            end_idx = content.find("-->", start_idx)
            if end_idx != -1:
                critique_request = content[start_idx + 4:end_idx].strip()
                message_type = critique_request
                critique_content = content[end_idx + 3:].strip()
                critique_messages.append(
                    ChatMessage(role_name=self.role_name,
                                role_type=self.role_type,
                                meta_dict=None,
                                role="assistant",
                                content=critique_content))
                content = content[:start_idx].strip()

        response_message = ChatMessage(
            role_name=self.role_name,
            role_type=self.role_type,
            meta_dict=None,
            role="assistant",
            content=content,
        )

        output_messages = [response_message]
        if len(critique_messages) > 0:
            output_messages.extend(critique_messages)

        self.update_messages(response_message)

        return ChatAgentResponse(
            msgs=output_messages,
            terminated=False,
            info=self.get_info(
                id=getattr(response, "id", None),
                usage={
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens,
                    "total_tokens": total_tokens,
                },
                termination_reasons=termination_reasons,
                num_tokens=num_tokens,
            ),
        )

    def __repr__(self) -> str:
        r"""Returns a string representation of the :obj:`ChatAgent`.

        Returns:
            str: The string representation of the :obj:`ChatAgent`.
        """
        return f"ChatAgent({self.role_name}, {self.role_type}, {self.model})"
