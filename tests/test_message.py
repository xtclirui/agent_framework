"""
Unit tests for the Message module.
"""

import pytest
from datetime import datetime
from agentframework.message import Message, MessageRole


def test_message_creation():
    """Test basic message creation."""
    msg = Message(role=MessageRole.USER, content="Hello")
    assert msg.role == MessageRole.USER
    assert msg.content == "Hello"
    assert isinstance(msg.timestamp, datetime)
    assert msg.metadata == {}


def test_message_with_metadata():
    """Test message creation with metadata."""
    metadata = {"key": "value", "num": 42}
    msg = Message(
        role=MessageRole.AGENT,
        content="Response",
        metadata=metadata
    )
    assert msg.metadata == metadata


def test_message_str():
    """Test message string representation."""
    msg = Message(role=MessageRole.USER, content="Test message")
    assert str(msg) == "[user] Test message"


def test_message_to_dict():
    """Test message to dictionary conversion."""
    msg = Message(role=MessageRole.SYSTEM, content="System message")
    msg_dict = msg.to_dict()
    
    assert msg_dict["role"] == "system"
    assert msg_dict["content"] == "System message"
    assert "timestamp" in msg_dict
    assert msg_dict["metadata"] == {}


def test_all_message_roles():
    """Test all message role types."""
    roles = [MessageRole.SYSTEM, MessageRole.USER, MessageRole.AGENT, MessageRole.TOOL]
    
    for role in roles:
        msg = Message(role=role, content=f"Test for {role.value}")
        assert msg.role == role
