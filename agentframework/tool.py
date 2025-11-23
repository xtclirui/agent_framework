"""
Tool module for agent capabilities.

Defines the Tool interface for extending agent functionality.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class Tool(ABC):
    """
    Abstract base class for agent tools.
    
    Tools extend agent capabilities by providing specific functions
    that agents can call to accomplish tasks.
    """
    
    def __init__(self, name: str, description: str):
        """
        Initialize the tool.
        
        Args:
            name: The name of the tool
            description: A description of what the tool does
        """
        self.name = name
        self.description = description
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool with given parameters.
        
        Args:
            **kwargs: Parameters for tool execution
            
        Returns:
            The result of the tool execution
        """
        pass
    
    def get_info(self) -> Dict[str, str]:
        """
        Get information about the tool.
        
        Returns:
            Dictionary with tool name and description
        """
        return {
            "name": self.name,
            "description": self.description
        }
    
    def __str__(self) -> str:
        """Return a string representation of the tool."""
        return f"Tool({self.name})"
