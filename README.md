# Voxentia Core

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Core framework for building intelligent, modular AI agents.

## 🎯 Mission

Voxentia Core provides the foundation for creating AI agents that are:
- **Modular**: Plug-and-play tools and memory systems
- **Extensible**: Easy to add new capabilities
- **Testable**: Built with testing in mind
- **Privacy-first**: Your data, your control

## 📦 Architecture

```
core/
├── agent/ # Agent base classes and implementations
├── tools/ # Reusable tool interfaces and implementations
├── memory/ # Memory management and context handling
└── utils/ # Shared utilities
```

## 🚀 Quick Start

```python
from src.agent.base_agent import BaseAgent

class MyAgent(BaseAgent):
    def run(self, user_input: str, **kwargs) -> str:
        # Your agent logic here
        return f"Echo: {user_input}"

agent = MyAgent(name="EchoBot")
response = agent.run("Hello!")
print(response)  # Echo: Hello!
```

🛠️ Installation

```
# Clone the repository
git clone https://github.com/voxentia/core.git
cd core

# Install dependencies (optional)
pip install -r requirements.txt

# Run tests
pytest tests/
```

📄 License

MIT License — see LICENSE for details.