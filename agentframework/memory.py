"""
Memory module for agent context retention.

Provides memory storage for agents to maintain conversation history.
"""

from typing import List, Optional
from .message import Message


class Memory:
    """
    Memory storage for agent conversations and context.
    
    Stores messages and provides retrieval mechanisms for agent context.
    """
    
    def __init__(self, max_messages: Optional[int] = None):
        """
        Initialize the memory.
        
        Args:
            max_messages: Maximum number of messages to store (None for unlimited)
        """
        self.max_messages = max_messages
        self.messages: List[Message] = []
    
    def add(self, message: Message) -> None:
        """
        Add a message to memory.
        
        Args:
            message: The message to add
        """
        self.messages.append(message)
        
        # Trim if exceeding max_messages
        if self.max_messages and len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    def get_all(self) -> List[Message]:
        """
        Retrieve all messages from memory.
        
        Returns:
            List of all stored messages
        """
        return self.messages.copy()
    
    def get_recent(self, n: int) -> List[Message]:
        """
        Retrieve the n most recent messages.
        
        Args:
            n: Number of recent messages to retrieve
            
        Returns:
            List of n most recent messages
        """
        return self.messages[-n:] if n > 0 else []
    
    def clear(self) -> None:
        """Clear all messages from memory."""
        self.messages.clear()
    
    def __len__(self) -> int:
        """Return the number of messages in memory."""
        return len(self.messages)
    
    def __str__(self) -> str:
        """Return a string representation of memory."""
        return f"Memory({len(self.messages)} messages)"
