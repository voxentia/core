import pytest
from src.agent.base_agent import BaseAgent, Message


class TestAgent(BaseAgent):
    """Concrete implementation for testing."""
    
    def run(self, user_input: str, **kwargs) -> str:
        return f"Processed: {user_input}"


def test_agent_initialization():
    agent = TestAgent(name="TestBot", description="A test agent")
    assert agent.name == "TestBot"
    assert agent.description == "A test agent"
    assert len(agent.memory) == 0


def test_agent_run():
    agent = TestAgent(name="TestBot")
    result = agent.run("Hello")
    assert result == "Processed: Hello"


def test_memory_add_and_trim():
    agent = TestAgent(name="TestBot", max_memory=3)
    
    # Add 5 messages
    for i in range(5):
        agent.add_message("user", f"Message {i}")
    
    # Should keep only last 3
    assert len(agent.memory) == 3
    assert agent.memory[0].content == "Message 2"


def test_context_format():
    agent = TestAgent(name="TestBot")
    agent.add_message("user", "Hello")
    agent.add_message("assistant", "Hi there")
    
    context = agent.get_context()
    assert len(context) == 2
    assert context[0]["role"] == "user"
    assert context[1]["role"] == "assistant"