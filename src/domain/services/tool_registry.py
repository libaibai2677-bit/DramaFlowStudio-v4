# 🧩 Tool Registry (Agent Capability Layer)
# Enables future Agent / Tool-Calling architecture

from typing import Callable, Dict, Any


class ToolRegistry:
    """
    Central registry for internal tools.
    This is the foundation for agent-based execution.
    """

    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self.tools[name] = func

    def execute(self, name: str, **kwargs) -> Any:
        if name not in self.tools:
            return {"error": f"Tool '{name}' not found"}

        return self.tools[name](**kwargs)

    def list_tools(self):
        return list(self.tools.keys())
