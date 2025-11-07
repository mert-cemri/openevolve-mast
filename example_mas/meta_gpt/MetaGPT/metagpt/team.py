#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/12 00:30
@Author  : alexanderwu
@File    : team.py
@Modified By: mashenquan, 2023/11/27. Add an archiving operation after completing the project, as specified in
        Section 2.2.3.3 of RFC 135.
"""

import warnings
from pathlib import Path
from typing import Any, Optional
import datetime
import os

from pydantic import BaseModel, ConfigDict, Field

from metagpt.actions import UserRequirement
from metagpt.const import MESSAGE_ROUTE_TO_ALL, SERDESER_PATH
from metagpt.context import Context
from metagpt.environment import Environment
from metagpt.logs import logger
from metagpt.roles import Role
from metagpt.schema import Message
from metagpt.utils.common import (
    NoMoneyException,
    read_json_file,
    serialize_decorator,
    write_json_file,
)


class MessageLogger:
    """A simple logger for messages in the environment"""
    
    def __init__(self, log_file: str):
        self.log_file = log_file
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        # Add header to log file
        with open(self.log_file, 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"=== MetaGPT Agent Communication Log - Started at {timestamp} ===\n\n")
        
        logger.info(f"Successfully created log file at {self.log_file}")
    
    def log_message(self, message: Message):
        """Log a message to the log file"""
        try:
            with open(self.log_file, 'a') as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] FROM: {message.role} TO: {message.send_to or 'ALL'}\n")
                
                # Handle cause_by safely - it could be a class, string, or None
                cause_by = message.cause_by
                if cause_by is None:
                    cause_str = "None"
                elif hasattr(cause_by, "__name__"):
                    cause_str = cause_by.__name__
                else:
                    cause_str = str(cause_by)
                    
                f.write(f"ACTION: {cause_str}\n")
                f.write(f"CONTENT:\n{message.content}\n")
                f.write("-" * 80 + "\n\n")
            logger.debug(f"Logged message from {message.role} to log file")
        except Exception as e:
            logger.error(f"Failed to write to log file {self.log_file}: {e}")
    
    def close(self):
        """Close the log file with a footer"""
        try:
            with open(self.log_file, 'a') as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"\n=== Communication Log Ended at {timestamp} ===\n")
        except Exception as e:
            logger.error(f"Failed to close log file {self.log_file}: {e}")


class Team(BaseModel):
    """
    Team: Possesses one or more roles (agents), SOP (Standard Operating Procedures), and a env for instant messaging,
    dedicated to env any multi-agent activity, such as collaboratively writing executable code.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    env: Optional[Environment] = None
    investment: float = Field(default=10.0)
    idea: str = Field(default="")
    log_file: Optional[str] = Field(default=None)
    _message_logger: Optional[MessageLogger] = None

    def __init__(self, context: Context = None, log_file: str = None, **data: Any):
        super(Team, self).__init__(**data)
        ctx = context or Context()
        if not self.env:
            self.env = Environment(context=ctx)
        else:
            self.env.context = ctx  # The `env` object is allocated by deserialization
        if "roles" in data:
            self.hire(data["roles"])
        if "env_desc" in data:
            self.env.desc = data["env_desc"]
        self.log_file = log_file
        
        # Set up message logging
        if self.log_file:
            try:
                self._message_logger = MessageLogger(self.log_file)
                logger.info(f"Message logging enabled to {self.log_file}")
            except Exception as e:
                logger.error(f"Failed to set up logging to {self.log_file}: {e}")
                self.log_file = None

    def serialize(self, stg_path: Path = None):
        stg_path = SERDESER_PATH.joinpath("team") if stg_path is None else stg_path
        team_info_path = stg_path.joinpath("team.json")
        serialized_data = self.model_dump()
        serialized_data["context"] = self.env.context.serialize()

        write_json_file(team_info_path, serialized_data)

    @classmethod
    def deserialize(cls, stg_path: Path, context: Context = None) -> "Team":
        """stg_path = ./storage/team"""
        # recover team_info
        team_info_path = stg_path.joinpath("team.json")
        if not team_info_path.exists():
            raise FileNotFoundError(
                "recover storage meta file `team.json` not exist, " "not to recover and please start a new project."
            )

        team_info: dict = read_json_file(team_info_path)
        ctx = context or Context()
        ctx.deserialize(team_info.pop("context", None))
        team = Team(**team_info, context=ctx)
        return team

    def hire(self, roles: list[Role]):
        """Hire roles to cooperate"""
        self.env.add_roles(roles)

    @property
    def cost_manager(self):
        """Get cost manager"""
        return self.env.context.cost_manager

    def invest(self, investment: float):
        """Invest company. raise NoMoneyException when exceed max_budget."""
        self.investment = investment
        self.cost_manager.max_budget = investment
        logger.info(f"Investment: ${investment}.")

    def _check_balance(self):
        if self.cost_manager.total_cost >= self.cost_manager.max_budget:
            raise NoMoneyException(self.cost_manager.total_cost, f"Insufficient funds: {self.cost_manager.max_budget}")

    def run_project(self, idea, send_to: str = ""):
        """Run a project from publishing user requirement."""
        self.idea = idea

        # Human requirement.
        message = Message(role="Human", content=idea, cause_by=UserRequirement, send_to=send_to or MESSAGE_ROUTE_TO_ALL)
        
        # Log the message if logging is enabled
        if self._message_logger:
            self._message_logger.log_message(message)
            
        self.env.publish_message(message, peekable=False)

    def start_project(self, idea, send_to: str = ""):
        """
        Deprecated: This method will be removed in the future.
        Please use the `run_project` method instead.
        """
        warnings.warn(
            "The 'start_project' method is deprecated and will be removed in the future. "
            "Please use the 'run_project' method instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.run_project(idea=idea, send_to=send_to)

    @serialize_decorator
    async def run(self, n_round=3, idea="", send_to="", auto_archive=True):
        """Run company until target round or no money"""
        if idea:
            self.run_project(idea=idea, send_to=send_to)

        # Store the original history for comparison
        last_history_length = len(self.env.history) if hasattr(self.env, 'history') else 0
        
        while n_round > 0:
            if self.env.is_idle:
                logger.debug("All roles are idle.")
                break
            n_round -= 1
            self._check_balance()
            
            # Run the environment
            await self.env.run()
            
            # Check for new messages in the history
            if self._message_logger and hasattr(self.env, 'history'):
                current_history = self.env.history
                if len(current_history) > last_history_length:
                    # Extract new messages from history
                    new_history = current_history[last_history_length:]
                    logger.debug(f"New history: {new_history}")
                    
                    # Parse and log new messages
                    # This is a simple approach - we're just logging the raw history
                    with open(self.log_file, 'a') as f:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"[{timestamp}] NEW MESSAGES:\n")
                        f.write(new_history)
                        f.write("\n" + "-" * 80 + "\n\n")
                    
                    # Update the last history length
                    last_history_length = len(current_history)
            
            logger.debug(f"max {n_round=} left.")
        
        # Close the log file if logging is enabled
        if self._message_logger:
            self._message_logger.close()
                
        self.env.archive(auto_archive)
        return self.env.history
