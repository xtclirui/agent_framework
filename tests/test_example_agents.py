"""
Tests for example agents.
"""

import pytest
from examples.example_agents import SimpleAgent, AssistantAgent, ConversationalAgent
from examples.example_tools import CalculatorTool, SearchTool


def test_simple_agent():
    """Test SimpleAgent basic functionality."""
    agent = SimpleAgent()
    response = agent.process("Hello")
    
    assert "Hello" in response
    assert "How can I help you?" in response


def test_simple_agent_name():
    """Test SimpleAgent has correct name."""
    agent = SimpleAgent()
    assert agent.name == "SimpleAgent"


def test_assistant_agent():
    """Test AssistantAgent basic functionality."""
    agent = AssistantAgent()
    response = agent.process("What can you do?")
    
    assert "assistant" in response.lower() or "tools" in response.lower()


def test_assistant_agent_with_calculator():
    """Test AssistantAgent recognizes calculator queries."""
    agent = AssistantAgent()
    agent.add_tool(CalculatorTool())
    
    response = agent.process("I need to calculate something")
    assert "calculator" in response.lower() or "calculate" in response.lower()


def test_assistant_agent_with_search():
    """Test AssistantAgent recognizes search queries."""
    agent = AssistantAgent()
    agent.add_tool(SearchTool())
    
    response = agent.process("I need to search for information")
    assert "search" in response.lower()


def test_conversational_agent():
    """Test ConversationalAgent tracks conversation count."""
    agent = ConversationalAgent()
    
    response1 = agent.process("First message")
    assert "Nice to meet you" in response1 or "First message" in response1
    
    response2 = agent.process("Second message")
    assert "#2" in response2 or "Second message" in response2


def test_conversational_agent_memory_limit():
    """Test ConversationalAgent respects memory limit."""
    agent = ConversationalAgent()
    assert agent.memory.max_messages == 10


def test_conversational_agent_multiple_messages():
    """Test ConversationalAgent handles multiple messages."""
    agent = ConversationalAgent()
    
    for i in range(3):
        agent.process(f"Message {i}")
    
    assert agent.conversation_count == 3
    assert len(agent.get_history()) == 6  # 3 user + 3 agent messages
