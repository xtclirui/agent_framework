"""
Example agents demonstrating the agent framework.

Shows how to create and customize agents with different capabilities.
"""

from agentframework import Agent, Message, MessageRole


class SimpleAgent(Agent):
    """A simple agent that echoes messages."""
    
    def __init__(self):
        super().__init__(
            name="SimpleAgent",
            description="A basic agent that responds to user messages"
        )
    
    def process(self, user_input: str) -> str:
        """
        Process user input with a simple greeting.
        
        Args:
            user_input: The user's input
            
        Returns:
            A friendly response
        """
        user_message = Message(role=MessageRole.USER, content=user_input)
        self.memory.add(user_message)
        
        response = f"Hello! You said: '{user_input}'. How can I help you?"
        
        agent_message = Message(role=MessageRole.AGENT, content=response)
        self.memory.add(agent_message)
        
        return response


class AssistantAgent(Agent):
    """An assistant agent that can use tools to help users."""
    
    def __init__(self):
        super().__init__(
            name="AssistantAgent",
            description="An intelligent assistant that can use tools to accomplish tasks"
        )
    
    def process(self, user_input: str) -> str:
        """
        Process user input and potentially use tools.
        
        Args:
            user_input: The user's input
            
        Returns:
            A helpful response
        """
        user_message = Message(role=MessageRole.USER, content=user_input)
        self.memory.add(user_message)
        
        # Simple keyword-based tool usage (in a real system, this would be more sophisticated)
        response = ""
        input_lower = user_input.lower()
        
        if "calculate" in input_lower or "add" in input_lower or "multiply" in input_lower:
            if "calculator" in self.tools:
                response = "I can help with calculations! Use the calculator tool to perform operations."
            else:
                response = "I would help with calculations, but I don't have a calculator tool."
        
        elif "search" in input_lower or "find" in input_lower:
            if "search" in self.tools:
                response = "I can help search for information! Use the search tool to find what you need."
            else:
                response = "I would help with searching, but I don't have a search tool."
        
        else:
            response = f"I'm an assistant agent with {len(self.tools)} tools available. How can I assist you?"
        
        agent_message = Message(role=MessageRole.AGENT, content=response)
        self.memory.add(agent_message)
        
        return response


class ConversationalAgent(Agent):
    """An agent that maintains conversation context."""
    
    def __init__(self):
        super().__init__(
            name="ConversationalAgent",
            description="An agent that remembers conversation history",
            max_memory=10  # Keep last 10 messages
        )
        self.conversation_count = 0
    
    def process(self, user_input: str) -> str:
        """
        Process user input with conversation awareness.
        
        Args:
            user_input: The user's input
            
        Returns:
            A contextual response
        """
        user_message = Message(role=MessageRole.USER, content=user_input)
        self.memory.add(user_message)
        
        self.conversation_count += 1
        
        if self.conversation_count == 1:
            response = f"Nice to meet you! You said: '{user_input}'"
        else:
            response = f"Thanks for message #{self.conversation_count}. You said: '{user_input}'"
        
        agent_message = Message(role=MessageRole.AGENT, content=response)
        self.memory.add(agent_message)
        
        return response
