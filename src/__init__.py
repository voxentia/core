"""
Voxentia Core — Modular framework for building intelligent AI agents.

Usage:
    from voxentia.agent import BaseAgent
    from voxentia.tools import BaseTool
"""

__version__ = "0.1.0"
__author__ = "Voxentia Team"
__email__ = "voxentia.lab@gmail.com"

from .agent.base_agent import BaseAgent, Message
from .tools.tool_interface import BaseTool
from .memory.memory_manager import MemoryManager

__all__ = [
    "BaseAgent",
    "Message", 
    "BaseTool",
    "MemoryManager",
    "__version__",
]