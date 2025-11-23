"""
Message module for agent communication.

Defines message types and roles for agent interactions.
"""

from enum import Enum
from typing import Any, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime


class MessageRole(Enum):
    """Defines the role of a message sender."""
    SYSTEM = "system"
    USER = "user"
    AGENT = "agent"
    TOOL = "tool"


@dataclass
class Message:
    """
    Represents a message in the agent framework.
    
    Attributes:
        role: The role of the message sender (system, user, agent, or tool)
        content: The content of the message
        metadata: Optional metadata associated with the message
        timestamp: Time when the message was created
    """
    role: MessageRole
    content: str
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __str__(self) -> str:
        """Return a string representation of the message."""
        return f"[{self.role.value}] {self.content}"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the message to a dictionary."""
        return {
            "role": self.role.value,
            "content": self.content,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat()
        }
