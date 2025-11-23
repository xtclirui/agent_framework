"""
Agent module - the core component of the framework.

Defines the base Agent class for creating intelligent agents.
"""

from typing import List, Optional, Dict, Any
from .message import Message, MessageRole
from .memory import Memory
from .tool import Tool


class Agent:
    """
    Base Agent class for the framework.
    
    An agent can receive messages, maintain conversation history,
    use tools, and generate responses.
    """
    
    def __init__(
        self, 
        name: str, 
        description: str = "",
        max_memory: Optional[int] = None
    ):
        """
        Initialize the agent.
        
        Args:
            name: The name of the agent
            description: A description of the agent's purpose
            max_memory: Maximum number of messages to store in memory
        """
        self.name = name
        self.description = description
        self.memory = Memory(max_messages=max_memory)
        self.tools: Dict[str, Tool] = {}
    
    def add_tool(self, tool: Tool) -> None:
        """
        Add a tool to the agent's capabilities.
        
        Args:
            tool: The tool to add
        """
        self.tools[tool.name] = tool
    
    def remove_tool(self, tool_name: str) -> bool:
        """
        Remove a tool from the agent's capabilities.
        
        Args:
            tool_name: The name of the tool to remove
            
        Returns:
            True if tool was removed, False if not found
        """
        if tool_name in self.tools:
            del self.tools[tool_name]
            return True
        return False
    
    def get_tools(self) -> List[str]:
        """
        Get list of available tool names.
        
        Returns:
            List of tool names
        """
        return list(self.tools.keys())
    
    def use_tool(self, tool_name: str, **kwargs) -> Any:
        """
        Use a specific tool.
        
        Args:
            tool_name: The name of the tool to use
            **kwargs: Parameters to pass to the tool
            
        Returns:
            The result of the tool execution
            
        Raises:
            ValueError: If the tool is not found
        """
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        tool = self.tools[tool_name]
        result = tool.execute(**kwargs)
        
        # Log tool usage in memory
        tool_message = Message(
            role=MessageRole.TOOL,
            content=f"Used tool '{tool_name}': {result}",
            metadata={"tool": tool_name, "kwargs": kwargs, "result": result}
        )
        self.memory.add(tool_message)
        
        return result
    
    def receive_message(self, message: Message) -> None:
        """
        Receive and store a message in memory.
        
        Args:
            message: The message to receive
        """
        self.memory.add(message)
    
    def process(self, user_input: str) -> str:
        """
        Process user input and generate a response.
        
        This is a simple implementation that can be overridden
        by subclasses for more sophisticated behavior.
        
        Args:
            user_input: The user's input string
            
        Returns:
            The agent's response
        """
        # Add user message to memory
        user_message = Message(role=MessageRole.USER, content=user_input)
        self.memory.add(user_message)
        
        # Generate response (simple echo in base implementation)
        response = f"{self.name} received: {user_input}"
        
        # Add agent response to memory
        agent_message = Message(role=MessageRole.AGENT, content=response)
        self.memory.add(agent_message)
        
        return response
    
    def get_history(self) -> List[Message]:
        """
        Get the conversation history.
        
        Returns:
            List of all messages in memory
        """
        return self.memory.get_all()
    
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.memory.clear()
    
    def __str__(self) -> str:
        """Return a string representation of the agent."""
        return f"Agent({self.name})"
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get information about the agent.
        
        Returns:
            Dictionary with agent information
        """
        return {
            "name": self.name,
            "description": self.description,
            "tools": [tool.get_info() for tool in self.tools.values()],
            "memory_size": len(self.memory)
        }
