"""
Integration tests for the agent framework.
"""

import pytest
from agentframework import Agent, Tool, Message, MessageRole


class CalculatorTool(Tool):
    """Calculator tool for testing."""
    
    def execute(self, operation: str, a: float, b: float) -> float:
        if operation == "add":
            return a + b
        elif operation == "multiply":
            return a * b
        else:
            raise ValueError(f"Unknown operation: {operation}")


def test_agent_with_calculator():
    """Test agent using calculator tool."""
    agent = Agent(name="MathAgent")
    calc = CalculatorTool(name="calculator", description="Math operations")
    agent.add_tool(calc)
    
    result1 = agent.use_tool("calculator", operation="add", a=5, b=3)
    assert result1 == 8
    
    result2 = agent.use_tool("calculator", operation="multiply", a=4, b=7)
    assert result2 == 28


def test_agent_conversation_flow():
    """Test a complete conversation flow."""
    agent = Agent(name="ChatAgent")
    
    # Simulate a conversation
    response1 = agent.process("Hello")
    assert "Hello" in response1
    
    response2 = agent.process("How are you?")
    assert "How are you?" in response2
    
    # Check history
    history = agent.get_history()
    assert len(history) == 4  # 2 user + 2 agent messages


def test_multiple_tools():
    """Test agent with multiple tools."""
    agent = Agent(name="MultiToolAgent")
    
    calc = CalculatorTool(name="calculator", description="Math")
    agent.add_tool(calc)
    
    class StringTool(Tool):
        def execute(self, text: str) -> str:
            return text.upper()
    
    string_tool = StringTool(name="uppercase", description="Uppercase text")
    agent.add_tool(string_tool)
    
    assert len(agent.get_tools()) == 2
    
    result1 = agent.use_tool("calculator", operation="add", a=1, b=2)
    assert result1 == 3
    
    result2 = agent.use_tool("uppercase", text="hello")
    assert result2 == "HELLO"


def test_agent_memory_limit():
    """Test agent with limited memory."""
    agent = Agent(name="LimitedAgent", max_memory=4)
    
    for i in range(5):
        agent.process(f"Message {i}")
    
    # Should only keep last 4 messages
    history = agent.get_history()
    assert len(history) == 4


def test_message_metadata_preservation():
    """Test that message metadata is preserved."""
    agent = Agent(name="MetaAgent")
    
    msg = Message(
        role=MessageRole.USER,
        content="Test",
        metadata={"source": "test", "id": 123}
    )
    
    agent.receive_message(msg)
    
    history = agent.get_history()
    assert history[0].metadata == {"source": "test", "id": 123}


def test_custom_agent_subclass():
    """Test creating a custom agent subclass."""
    
    class CustomAgent(Agent):
        def process(self, user_input: str) -> str:
            user_message = Message(role=MessageRole.USER, content=user_input)
            self.memory.add(user_message)
            
            response = f"Custom processing: {user_input.upper()}"
            
            agent_message = Message(role=MessageRole.AGENT, content=response)
            self.memory.add(agent_message)
            
            return response
    
    agent = CustomAgent(name="Custom")
    response = agent.process("hello")
    
    assert response == "Custom processing: HELLO"
    assert len(agent.get_history()) == 2
