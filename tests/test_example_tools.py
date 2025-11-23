"""
Tests for example tools.
"""

import pytest
from examples.example_tools import CalculatorTool, TextProcessorTool, SearchTool


def test_calculator_add():
    """Test calculator addition."""
    calc = CalculatorTool()
    result = calc.execute(operation="add", a=10, b=5)
    assert result == 15


def test_calculator_subtract():
    """Test calculator subtraction."""
    calc = CalculatorTool()
    result = calc.execute(operation="subtract", a=10, b=5)
    assert result == 5


def test_calculator_multiply():
    """Test calculator multiplication."""
    calc = CalculatorTool()
    result = calc.execute(operation="multiply", a=6, b=7)
    assert result == 42


def test_calculator_divide():
    """Test calculator division."""
    calc = CalculatorTool()
    result = calc.execute(operation="divide", a=20, b=4)
    assert result == 5.0


def test_calculator_divide_by_zero():
    """Test calculator division by zero error."""
    calc = CalculatorTool()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.execute(operation="divide", a=10, b=0)


def test_calculator_invalid_operation():
    """Test calculator with invalid operation."""
    calc = CalculatorTool()
    with pytest.raises(ValueError, match="Unsupported operation"):
        calc.execute(operation="power", a=2, b=3)


def test_text_processor_uppercase():
    """Test text processor uppercase."""
    processor = TextProcessorTool()
    result = processor.execute(operation="uppercase", text="hello world")
    assert result == "HELLO WORLD"


def test_text_processor_lowercase():
    """Test text processor lowercase."""
    processor = TextProcessorTool()
    result = processor.execute(operation="lowercase", text="HELLO WORLD")
    assert result == "hello world"


def test_text_processor_reverse():
    """Test text processor reverse."""
    processor = TextProcessorTool()
    result = processor.execute(operation="reverse", text="hello")
    assert result == "olleh"


def test_text_processor_word_count():
    """Test text processor word count."""
    processor = TextProcessorTool()
    result = processor.execute(operation="word_count", text="The quick brown fox")
    assert result == 4


def test_text_processor_invalid_operation():
    """Test text processor with invalid operation."""
    processor = TextProcessorTool()
    with pytest.raises(ValueError, match="Unsupported operation"):
        processor.execute(operation="invalid", text="test")


def test_search_tool_python():
    """Test search tool finding Python."""
    search = SearchTool()
    result = search.execute(query="python")
    assert "Python" in result
    assert "programming language" in result


def test_search_tool_agent():
    """Test search tool finding agent."""
    search = SearchTool()
    result = search.execute(query="What is an agent?")
    assert "agent" in result.lower()


def test_search_tool_not_found():
    """Test search tool with unknown query."""
    search = SearchTool()
    result = search.execute(query="unknown topic xyz")
    assert "No information found" in result
