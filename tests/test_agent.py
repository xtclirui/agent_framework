"""
Unit tests for the Agent module.
"""

import pytest
from agentframework.agent import Agent
from agentframework.message import Message, MessageRole
from agentframework.tool import Tool


class SimpleTool(Tool):
    """A simple tool for testing."""
    
    def execute(self, value: str) -> str:
        return f"Processed: {value}"


def test_agent_creation():
    """Test agent initialization."""
    agent = Agent(name="TestAgent", description="A test agent")
    assert agent.name == "TestAgent"
    assert agent.description == "A test agent"
    assert len(agent.tools) == 0


def test_agent_with_max_memory():
    """Test agent with maximum memory."""
    agent = Agent(name="TestAgent", max_memory=5)
    assert agent.memory.max_messages == 5


def test_add_tool():
    """Test adding a tool to agent."""
    agent = Agent(name="TestAgent")
    tool = SimpleTool(name="simple", description="Simple tool")
    
    agent.add_tool(tool)
    assert "simple" in agent.tools
    assert agent.get_tools() == ["simple"]


def test_remove_tool():
    """Test removing a tool from agent."""
    agent = Agent(name="TestAgent")
    tool = SimpleTool(name="simple", description="Simple tool")
    
    agent.add_tool(tool)
    assert "simple" in agent.tools
    
    result = agent.remove_tool("simple")
    assert result is True
    assert "simple" not in agent.tools


def test_remove_nonexistent_tool():
    """Test removing a tool that doesn't exist."""
    agent = Agent(name="TestAgent")
    result = agent.remove_tool("nonexistent")
    assert result is False


def test_use_tool():
    """Test using a tool."""
    agent = Agent(name="TestAgent")
    tool = SimpleTool(name="simple", description="Simple tool")
    agent.add_tool(tool)
    
    result = agent.use_tool("simple", value="test")
    assert result == "Processed: test"


def test_use_nonexistent_tool():
    """Test using a tool that doesn't exist."""
    agent = Agent(name="TestAgent")
    
    with pytest.raises(ValueError, match="Tool 'nonexistent' not found"):
        agent.use_tool("nonexistent", value="test")


def test_receive_message():
    """Test receiving a message."""
    agent = Agent(name="TestAgent")
    msg = Message(role=MessageRole.USER, content="Hello")
    
    agent.receive_message(msg)
    assert len(agent.memory) == 1
    assert agent.memory.get_all()[0] == msg


def test_process():
    """Test processing user input."""
    agent = Agent(name="TestAgent")
    response = agent.process("Hello agent")
    
    assert "TestAgent received: Hello agent" in response
    assert len(agent.memory) == 2  # User message + agent response


def test_get_history():
    """Test getting conversation history."""
    agent = Agent(name="TestAgent")
    
    agent.process("Message 1")
    agent.process("Message 2")
    
    history = agent.get_history()
    assert len(history) == 4  # 2 user messages + 2 agent responses


def test_clear_history():
    """Test clearing conversation history."""
    agent = Agent(name="TestAgent")
    
    agent.process("Message 1")
    assert len(agent.memory) > 0
    
    agent.clear_history()
    assert len(agent.memory) == 0


def test_agent_str():
    """Test agent string representation."""
    agent = Agent(name="MyAgent")
    assert str(agent) == "Agent(MyAgent)"


def test_get_info():
    """Test getting agent information."""
    agent = Agent(name="TestAgent", description="Test description")
    tool = SimpleTool(name="simple", description="Simple tool")
    agent.add_tool(tool)
    
    info = agent.get_info()
    assert info["name"] == "TestAgent"
    assert info["description"] == "Test description"
    assert len(info["tools"]) == 1
    assert info["tools"][0]["name"] == "simple"


def test_tool_usage_in_memory():
    """Test that tool usage is logged in memory."""
    agent = Agent(name="TestAgent")
    tool = SimpleTool(name="simple", description="Simple tool")
    agent.add_tool(tool)
    
    agent.use_tool("simple", value="test")
    
    messages = agent.get_history()
    assert len(messages) == 1
    assert messages[0].role == MessageRole.TOOL
