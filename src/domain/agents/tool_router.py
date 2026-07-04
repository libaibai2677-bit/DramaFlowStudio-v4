# 🧭 Tool Router (Intelligent Capability Selection Layer)
# Decides which tool should be used: RAG / Web / Internal Tools

from typing import Dict, Any

from src.domain.tools.web_search_tool import WebSearchTool
from src.domain.services.tool_registry import ToolRegistry


class ToolRouter:
    """
    Central decision layer for tool selection.

    Bridges:
    - reasoning (LLM)
    - execution (tools)
    - external knowledge (web)
    """

    def __init__(self, tools: ToolRegistry, web_tool: WebSearchTool = None):
        self.tools = tools
        self.web_tool = web_tool or WebSearchTool()

    def route(self, query: str) -> Dict[str, Any]:
        q = query.lower()

        # 🌐 External knowledge needed
        if any(k in q for k in ["latest", "news", "today", "price", "who is", "what is"]):
            return {
                "type": "web",
                "tool": "web_search",
                "reason": "external_information_detected"
            }

        # 🧩 Internal tool execution
        if "tool:" in q:
            tool_name = q.split("tool:")[-1].strip()
            return {
                "type": "internal_tool",
                "tool": tool_name,
                "reason": "explicit_tool_call"
            }

        # 📚 Default to RAG / internal reasoning
        return {
            "type": "rag",
            "tool": None,
            "reason": "default_internal_reasoning"
        }

    def execute(self, route: Dict[str, Any], query: str) -> Any:
        if route["type"] == "web":
            return self.web_tool.search(query)

        if route["type"] == "internal_tool":
            return self.tools.execute(route["tool"])

        return {
            "type": "rag_fallback",
            "query": query
        }