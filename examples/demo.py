"""
Demo script showcasing the AgentFramework.

This script demonstrates the basic usage of the framework.
"""

from agentframework import Agent, Message, MessageRole
from examples.example_tools import CalculatorTool, TextProcessorTool, SearchTool
from examples.example_agents import SimpleAgent, AssistantAgent, ConversationalAgent


def print_separator(title=""):
    """Print a visual separator."""
    if title:
        print(f"\n{'='*60}")
        print(f" {title}")
        print(f"{'='*60}\n")
    else:
        print(f"{'='*60}\n")


def demo_basic_agent():
    """Demonstrate basic agent functionality."""
    print_separator("Demo 1: Basic Agent")
    
    agent = Agent(name="BasicBot", description="A basic agent")
    print(f"Created agent: {agent}")
    print(f"Agent info: {agent.get_info()}\n")
    
    # Process messages
    response = agent.process("Hello, agent!")
    print(f"User: Hello, agent!")
    print(f"Agent: {response}\n")
    
    # Check history
    print(f"Conversation history ({len(agent.get_history())} messages):")
    for msg in agent.get_history():
        print(f"  {msg}")


def demo_agent_with_tools():
    """Demonstrate agent with tools."""
    print_separator("Demo 2: Agent with Tools")
    
    agent = Agent(name="ToolBot", description="An agent with tools")
    
    # Add tools
    agent.add_tool(CalculatorTool())
    agent.add_tool(TextProcessorTool())
    
    print(f"Agent tools: {agent.get_tools()}\n")
    
    # Use calculator
    result = agent.use_tool("calculator", operation="add", a=10, b=5)
    print(f"Calculator: 10 + 5 = {result}\n")
    
    result = agent.use_tool("calculator", operation="multiply", a=7, b=3)
    print(f"Calculator: 7 * 3 = {result}\n")
    
    # Use text processor
    result = agent.use_tool("text_processor", operation="uppercase", text="hello world")
    print(f"Text processor (uppercase): {result}\n")
    
    result = agent.use_tool("text_processor", operation="word_count", text="The quick brown fox")
    print(f"Text processor (word count): {result} words\n")


def demo_simple_agent():
    """Demonstrate SimpleAgent."""
    print_separator("Demo 3: Simple Agent")
    
    agent = SimpleAgent()
    print(f"Agent: {agent.name}")
    print(f"Description: {agent.description}\n")
    
    response = agent.process("I need help with something")
    print(f"User: I need help with something")
    print(f"Agent: {response}\n")


def demo_assistant_agent():
    """Demonstrate AssistantAgent with tools."""
    print_separator("Demo 4: Assistant Agent")
    
    agent = AssistantAgent()
    agent.add_tool(CalculatorTool())
    agent.add_tool(SearchTool())
    
    print(f"Agent: {agent.name}")
    print(f"Available tools: {agent.get_tools()}\n")
    
    # Test different queries
    queries = [
        "Can you help me calculate something?",
        "I need to search for information",
        "What can you do?",
    ]
    
    for query in queries:
        response = agent.process(query)
        print(f"User: {query}")
        print(f"Agent: {response}\n")


def demo_conversational_agent():
    """Demonstrate ConversationalAgent."""
    print_separator("Demo 5: Conversational Agent")
    
    agent = ConversationalAgent()
    print(f"Agent: {agent.name}")
    print(f"Max memory: {agent.memory.max_messages} messages\n")
    
    messages = [
        "Hello!",
        "How are you?",
        "Tell me about yourself",
        "Goodbye!",
    ]
    
    for msg in messages:
        response = agent.process(msg)
        print(f"User: {msg}")
        print(f"Agent: {response}\n")
    
    print(f"Total messages in history: {len(agent.get_history())}")


def demo_search_tool():
    """Demonstrate search tool functionality."""
    print_separator("Demo 6: Search Tool")
    
    agent = Agent(name="SearchBot")
    agent.add_tool(SearchTool())
    
    queries = ["python", "agent", "framework", "unknown topic"]
    
    for query in queries:
        result = agent.use_tool("search", query=query)
        print(f"Query: {query}")
        print(f"Result: {result}\n")


def main():
    """Run all demonstrations."""
    print("\n" + "="*60)
    print(" AgentFramework Demonstration")
    print(" A Simple Example of a Common Agent Framework")
    print("="*60)
    
    try:
        demo_basic_agent()
        demo_agent_with_tools()
        demo_simple_agent()
        demo_assistant_agent()
        demo_conversational_agent()
        demo_search_tool()
        
        print_separator("Demo Complete")
        print("All demonstrations completed successfully!")
        
    except Exception as e:
        print(f"\nError during demonstration: {e}")
        raise


if __name__ == "__main__":
    main()
