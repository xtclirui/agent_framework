"""
Example tools for the agent framework.

Demonstrates how to create custom tools for agents.
"""

from agentframework.tool import Tool


class CalculatorTool(Tool):
    """A simple calculator tool for basic arithmetic operations."""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs basic arithmetic operations (add, subtract, multiply, divide)"
        )
    
    def execute(self, operation: str, a: float, b: float) -> float:
        """
        Execute a calculation.
        
        Args:
            operation: The operation to perform (add, subtract, multiply, divide)
            a: First number
            b: Second number
            
        Returns:
            The result of the calculation
            
        Raises:
            ValueError: If operation is not supported or division by zero
        """
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError(f"Unsupported operation: {operation}")


class TextProcessorTool(Tool):
    """A tool for basic text processing operations."""
    
    def __init__(self):
        super().__init__(
            name="text_processor",
            description="Performs text processing operations (uppercase, lowercase, reverse, word_count)"
        )
    
    def execute(self, operation: str, text: str) -> any:
        """
        Execute a text processing operation.
        
        Args:
            operation: The operation to perform
            text: The text to process
            
        Returns:
            The result of the operation
            
        Raises:
            ValueError: If operation is not supported
        """
        if operation == "uppercase":
            return text.upper()
        elif operation == "lowercase":
            return text.lower()
        elif operation == "reverse":
            return text[::-1]
        elif operation == "word_count":
            return len(text.split())
        else:
            raise ValueError(f"Unsupported operation: {operation}")


class SearchTool(Tool):
    """A mock search tool for demonstration."""
    
    def __init__(self):
        super().__init__(
            name="search",
            description="Searches for information (mock implementation)"
        )
        # Mock knowledge base
        self.knowledge_base = {
            "python": "Python is a high-level programming language.",
            "agent": "An agent is an autonomous entity that can perceive and act.",
            "framework": "A framework is a reusable software structure.",
        }
    
    def execute(self, query: str) -> str:
        """
        Execute a search query.
        
        Args:
            query: The search query
            
        Returns:
            The search result
        """
        query_lower = query.lower()
        for key, value in self.knowledge_base.items():
            if key in query_lower:
                return value
        return f"No information found for: {query}"
