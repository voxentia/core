"""
Memory management for Voxentia agents.
"""

from typing import List, Optional
from src.agent.base_agent import Message


class MemoryManager:
    """Manages agent memory with advanced features."""
    
    def __init__(self, max_messages: int = 50):
        self.max_messages = max_messages
        self.messages: List[Message] = []
    
    def add(self, message: Message):
        """Add message with automatic trimming."""
        self.messages.append(message)
        self._trim()
    
    def _trim(self):
        """Remove oldest messages if over limit."""
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    def get_all(self) -> List[Message]:
        """Get all messages."""
        return self.messages.copy()
    
    def clear(self):
        """Clear all messages."""
        self.messages = []