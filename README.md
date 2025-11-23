# AgentFramework

A simple example of a common agent framework that provides the essential building blocks for creating intelligent agents.

## Overview

AgentFramework is a lightweight, extensible Python framework for building autonomous agents. It provides:

- **Agent Base Class**: Core agent implementation with message processing and tool management
- **Tool System**: Extensible interface for adding capabilities to agents
- **Memory Management**: Conversation history and context retention
- **Message Handling**: Structured communication between users, agents, and tools

## Features

- ✅ Simple and intuitive API
- ✅ Tool/action system for extending agent capabilities
- ✅ Built-in memory management with configurable limits
- ✅ Message-based communication with role support
- ✅ Easy to extend and customize
- ✅ Comprehensive test coverage
- ✅ Example agents and tools included

## Installation

```bash
# Clone the repository
git clone https://github.com/xtclirui/AgentFramework.git
cd AgentFramework

# Install the package
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"
```

## Quick Start

### Basic Agent

```python
from agentframework import Agent

# Create a simple agent
agent = Agent(name="MyAgent", description="A helpful assistant")

# Process user input
response = agent.process("Hello, agent!")
print(response)

# View conversation history
for message in agent.get_history():
    print(message)
```

### Agent with Tools

```python
from agentframework import Agent, Tool

# Define a custom tool
class CalculatorTool(Tool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs basic math operations"
        )
    
    def execute(self, operation: str, a: float, b: float) -> float:
        if operation == "add":
            return a + b
        elif operation == "multiply":
            return a * b
        # ... more operations

# Create agent and add tool
agent = Agent(name="MathBot")
agent.add_tool(CalculatorTool())

# Use the tool
result = agent.use_tool("calculator", operation="add", a=10, b=5)
print(f"Result: {result}")  # Output: Result: 15
```

### Custom Agent

```python
from agentframework import Agent, Message, MessageRole

class CustomAgent(Agent):
    def process(self, user_input: str) -> str:
        # Add user message to memory
        user_message = Message(role=MessageRole.USER, content=user_input)
        self.memory.add(user_message)
        
        # Custom processing logic
        response = f"Processed: {user_input.upper()}"
        
        # Add agent response to memory
        agent_message = Message(role=MessageRole.AGENT, content=response)
        self.memory.add(agent_message)
        
        return response

# Use custom agent
agent = CustomAgent(name="Custom")
print(agent.process("hello"))  # Output: Processed: HELLO
```

## Architecture

### Core Components

#### Agent
The `Agent` class is the main component that:
- Processes user messages
- Maintains conversation history via `Memory`
- Manages and executes `Tools`
- Generates responses

#### Tool
The `Tool` abstract class defines the interface for agent capabilities:
- `execute(**kwargs)`: Implement tool-specific logic
- `get_info()`: Returns tool metadata

#### Memory
The `Memory` class stores conversation history:
- Configurable message limits
- Recent message retrieval
- Full history access

#### Message
The `Message` dataclass represents communication:
- Role-based (SYSTEM, USER, AGENT, TOOL)
- Content and metadata
- Timestamp tracking

## Examples

The `examples/` directory contains:

- **demo.py**: Comprehensive demonstration of all features
- **example_agents.py**: Pre-built agent implementations
  - `SimpleAgent`: Basic conversational agent
  - `AssistantAgent`: Tool-aware assistant
  - `ConversationalAgent`: Context-aware agent
- **example_tools.py**: Useful tool implementations
  - `CalculatorTool`: Math operations
  - `TextProcessorTool`: Text manipulation
  - `SearchTool`: Information retrieval (mock)

### Running the Demo

```bash
cd AgentFramework
python -m examples.demo
```

This will run all demonstrations showing various framework capabilities.

## Testing

The framework includes comprehensive tests:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=agentframework --cov-report=html

# Run specific test file
pytest tests/test_agent.py
```

Test files:
- `test_agent.py`: Agent class tests
- `test_tool.py`: Tool interface tests
- `test_memory.py`: Memory management tests
- `test_message.py`: Message handling tests
- `test_integration.py`: Integration tests
- `test_example_tools.py`: Example tool tests
- `test_example_agents.py`: Example agent tests

## API Reference

### Agent

```python
Agent(name: str, description: str = "", max_memory: Optional[int] = None)
```

**Methods:**
- `add_tool(tool: Tool)`: Add a tool to the agent
- `remove_tool(tool_name: str) -> bool`: Remove a tool
- `get_tools() -> List[str]`: Get list of tool names
- `use_tool(tool_name: str, **kwargs) -> Any`: Execute a tool
- `process(user_input: str) -> str`: Process user input and generate response
- `receive_message(message: Message)`: Add a message to memory
- `get_history() -> List[Message]`: Get conversation history
- `clear_history()`: Clear conversation history
- `get_info() -> Dict[str, Any]`: Get agent information

### Tool

```python
Tool(name: str, description: str)
```

**Methods:**
- `execute(**kwargs) -> Any`: Execute the tool (abstract, must implement)
- `get_info() -> Dict[str, str]`: Get tool information

### Memory

```python
Memory(max_messages: Optional[int] = None)
```

**Methods:**
- `add(message: Message)`: Add a message
- `get_all() -> List[Message]`: Get all messages
- `get_recent(n: int) -> List[Message]`: Get n most recent messages
- `clear()`: Clear all messages
- `__len__() -> int`: Get message count

### Message

```python
Message(role: MessageRole, content: str, metadata: Optional[Dict[str, Any]] = None)
```

**Attributes:**
- `role`: MessageRole (SYSTEM, USER, AGENT, TOOL)
- `content`: Message content string
- `metadata`: Optional dictionary for additional data
- `timestamp`: Automatic timestamp

**Methods:**
- `to_dict() -> Dict[str, Any]`: Convert to dictionary

## Use Cases

- **Chatbots**: Build conversational AI assistants
- **Task Automation**: Create agents that automate workflows
- **Information Retrieval**: Develop agents that search and process data
- **Multi-Agent Systems**: Foundation for agent collaboration
- **Research**: Experiment with agent architectures and behaviors

## Design Philosophy

1. **Simplicity**: Easy to understand and use
2. **Extensibility**: Simple to extend with custom agents and tools
3. **Modularity**: Components can be used independently
4. **Minimal Dependencies**: Core framework has no external dependencies
5. **Best Practices**: Follows Python conventions and patterns

## Contributing

Contributions are welcome! This is an example framework designed to demonstrate common agent patterns.

## License

This project is open source and available for educational and demonstration purposes.

## Project Structure

```
AgentFramework/
├── agentframework/          # Core framework package
│   ├── __init__.py         # Package exports
│   ├── agent.py            # Agent base class
│   ├── tool.py             # Tool interface
│   ├── memory.py           # Memory management
│   └── message.py          # Message types
├── examples/               # Example implementations
│   ├── demo.py            # Demonstration script
│   ├── example_agents.py  # Example agent classes
│   └── example_tools.py   # Example tool classes
├── tests/                 # Test suite
│   ├── test_agent.py
│   ├── test_tool.py
│   ├── test_memory.py
│   ├── test_message.py
│   ├── test_integration.py
│   ├── test_example_tools.py
│   └── test_example_agents.py
├── setup.py              # Package configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## FAQ

**Q: Can I use this in production?**  
A: This is a simple example framework for educational purposes. For production use, consider more robust frameworks like LangChain, AutoGPT, or similar.

**Q: How do I add AI/LLM capabilities?**  
A: You can extend the `Agent` class to integrate with APIs like OpenAI, Anthropic, etc. in the `process()` method.

**Q: Can agents communicate with each other?**  
A: Yes! Create multiple agents and pass messages between them using the `Message` class.

**Q: How do I persist agent memory?**  
A: Extend the `Memory` class to save/load messages to/from a database or file system.

## Acknowledgments

This framework demonstrates common patterns found in agent architectures and is inspired by various AI agent frameworks in the ecosystem.