"""
Base agent module for Voxentia AI framework.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Message:
    """Represents a single message in agent memory."""
    role: str  # 'user', 'assistant', 'system'
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Optional[Dict[str, Any]] = None


class BaseAgent(ABC):
    """
    Abstract base class for all Voxentia AI agents.
    
    Provides core functionality:
    - Message handling and memory management
    - Tool registration and execution
    - LLM abstraction layer
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        max_memory: int = 50
    ):
        self.name = name
        self.description = description
        self.max_memory = max_memory
        self.memory: List[Message] = []
        self.tools: Dict[str, callable] = {}
        
    @abstractmethod
    def run(self, user_input: str, **kwargs) -> str:
        """
        Process user input and return agent response.
        
        Args:
            user_input: The user's message
            **kwargs: Additional context or parameters
            
        Returns:
            str: Agent's response
        """
        pass
    
    def add_message(self, role: str, content: str, metadata: Optional[Dict] = None):
        """Add a message to agent memory with automatic trimming."""
        self.memory.append(Message(role=role, content=content, metadata=metadata))
        
        # Trim memory if exceeds limit
        if len(self.memory) > self.max_memory:
            self.memory = self.memory[-self.max_memory:]
    
    def get_context(self) -> List[Dict[str, str]]:
        """Convert memory to LLM-friendly format."""
        return [
            {"role": msg.role, "content": msg.content}
            for msg in self.memory
        ]
    
    def register_tool(self, name: str, func: callable, description: str):
        """Register a tool that the agent can use."""
        self.tools[name] = {
            "func": func,
            "description": description
        }
    
    def execute_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a registered tool."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not registered")
        return self.tools[tool_name]["func"](**kwargs)
    
    def clear_memory(self):
        """Clear agent memory."""
        self.memory = []