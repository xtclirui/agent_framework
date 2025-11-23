"""
Unit tests for the Memory module.
"""

import pytest
from agentframework.memory import Memory
from agentframework.message import Message, MessageRole


def test_memory_creation():
    """Test memory initialization."""
    memory = Memory()
    assert len(memory) == 0
    assert memory.max_messages is None


def test_memory_with_max_messages():
    """Test memory with maximum message limit."""
    memory = Memory(max_messages=5)
    assert memory.max_messages == 5


def test_add_message():
    """Test adding messages to memory."""
    memory = Memory()
    msg = Message(role=MessageRole.USER, content="Test")
    
    memory.add(msg)
    assert len(memory) == 1
    assert memory.get_all()[0] == msg


def test_add_multiple_messages():
    """Test adding multiple messages."""
    memory = Memory()
    
    for i in range(5):
        msg = Message(role=MessageRole.USER, content=f"Message {i}")
        memory.add(msg)
    
    assert len(memory) == 5


def test_max_messages_limit():
    """Test that memory respects max_messages limit."""
    memory = Memory(max_messages=3)
    
    for i in range(5):
        msg = Message(role=MessageRole.USER, content=f"Message {i}")
        memory.add(msg)
    
    assert len(memory) == 3
    messages = memory.get_all()
    assert messages[0].content == "Message 2"
    assert messages[-1].content == "Message 4"


def test_get_recent():
    """Test getting recent messages."""
    memory = Memory()
    
    for i in range(5):
        msg = Message(role=MessageRole.USER, content=f"Message {i}")
        memory.add(msg)
    
    recent = memory.get_recent(3)
    assert len(recent) == 3
    assert recent[0].content == "Message 2"
    assert recent[-1].content == "Message 4"


def test_get_recent_more_than_available():
    """Test getting more recent messages than available."""
    memory = Memory()
    msg = Message(role=MessageRole.USER, content="Only one")
    memory.add(msg)
    
    recent = memory.get_recent(5)
    assert len(recent) == 1


def test_clear():
    """Test clearing memory."""
    memory = Memory()
    
    for i in range(3):
        msg = Message(role=MessageRole.USER, content=f"Message {i}")
        memory.add(msg)
    
    assert len(memory) == 3
    memory.clear()
    assert len(memory) == 0


def test_memory_str():
    """Test memory string representation."""
    memory = Memory()
    memory.add(Message(role=MessageRole.USER, content="Test"))
    assert str(memory) == "Memory(1 messages)"
