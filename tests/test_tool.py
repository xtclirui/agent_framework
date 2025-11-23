"""
Unit tests for the Tool module.
"""

import pytest
from agentframework.tool import Tool


class TestTool(Tool):
    """A simple test tool implementation."""
    
    def execute(self, value: int) -> int:
        """Double the input value."""
        return value * 2


def test_tool_creation():
    """Test tool initialization."""
    tool = TestTool(name="test_tool", description="A test tool")
    assert tool.name == "test_tool"
    assert tool.description == "A test tool"


def test_tool_execute():
    """Test tool execution."""
    tool = TestTool(name="test_tool", description="A test tool")
    result = tool.execute(value=5)
    assert result == 10


def test_tool_get_info():
    """Test getting tool information."""
    tool = TestTool(name="test_tool", description="A test tool")
    info = tool.get_info()
    
    assert info["name"] == "test_tool"
    assert info["description"] == "A test tool"


def test_tool_str():
    """Test tool string representation."""
    tool = TestTool(name="my_tool", description="Description")
    assert str(tool) == "Tool(my_tool)"


def test_abstract_tool_cannot_instantiate():
    """Test that Tool base class cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Tool(name="test", description="test")
