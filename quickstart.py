#!/usr/bin/env python3
"""
Quick start example for AgentFramework.

This script provides a minimal working example.
"""

from agentframework import Agent
from examples.example_tools import CalculatorTool, SearchTool

def main():
    print("=" * 60)
    print("AgentFramework Quick Start")
    print("=" * 60)
    print()
    
    # Create an agent
    print("1. Creating an agent...")
    agent = Agent(name="QuickBot", description="A quick start example agent")
    print(f"   ✓ Created: {agent}")
    print()
    
    # Add tools
    print("2. Adding tools...")
    agent.add_tool(CalculatorTool())
    agent.add_tool(SearchTool())
    print(f"   ✓ Tools: {', '.join(agent.get_tools())}")
    print()
    
    # Process a message
    print("3. Processing a message...")
    response = agent.process("Hello, QuickBot!")
    print(f"   User: Hello, QuickBot!")
    print(f"   Agent: {response}")
    print()
    
    # Use a tool
    print("4. Using the calculator tool...")
    result = agent.use_tool("calculator", operation="add", a=15, b=27)
    print(f"   15 + 27 = {result}")
    print()
    
    # Use another tool
    print("5. Using the search tool...")
    result = agent.use_tool("search", query="python")
    print(f"   Query: 'python'")
    print(f"   Result: {result}")
    print()
    
    # Check conversation history
    print("6. Viewing conversation history...")
    history = agent.get_history()
    print(f"   Total messages: {len(history)}")
    for i, msg in enumerate(history, 1):
        print(f"   {i}. {msg}")
    print()
    
    print("=" * 60)
    print("Quick start complete! 🎉")
    print()
    print("Next steps:")
    print("  - Read the README.md for detailed documentation")
    print("  - Run 'python -m examples.demo' for more examples")
    print("  - Create your own custom agents and tools")
    print("=" * 60)

if __name__ == "__main__":
    main()
