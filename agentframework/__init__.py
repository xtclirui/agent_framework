"""
AgentFramework - A simple example of a common agent framework.

This package provides a minimal yet functional agent framework with:
- Base Agent class for creating intelligent agents
- Tool system for extending agent capabilities
- Memory system for context retention
- Message-based communication
"""

__version__ = "0.1.0"

from .agent import Agent
from .tool import Tool
from .memory import Memory
from .message import Message, MessageRole

__all__ = ["Agent", "Tool", "Memory", "Message", "MessageRole"]
