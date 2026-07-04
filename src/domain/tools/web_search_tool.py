# 🌐 Web Search Tool (External Capability Layer)
# Adds optional internet search capability to Agent system

from typing import Dict, Any, List


class WebSearchTool:
    """
    External web search abstraction.
    In production, this can connect to:
    - Google Search API
    - Bing Search API
    - SerpAPI
    - Internal enterprise search gateway

    NOTE: This is a placeholder implementation.
    """

    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def search(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """
        Perform a web search.
        Currently returns a mocked response.
        """

        return {
            "query": query,
            "results": [
                {
                    "title": "Mock result 1",
                    "snippet": "This is a placeholder search result.",
                    "url": "https://example.com"
                },
                {
                    "title": "Mock result 2",
                    "snippet": "Replace with real search API integration.",
                    "url": "https://example.org"
                }
            ][:top_k],
            "source": "mock-web-search"
        }