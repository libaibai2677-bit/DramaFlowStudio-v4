# 🌐 Real Web Search Tool (Production External Knowledge Layer)
# Replaces mock search with real API integration (SerpAPI / Tavily / Bing / Custom)

import os
import requests
from typing import Dict, Any, List


class RealWebSearchTool:
    """
    Production-ready web search connector.

    Supported providers (configurable via env):
    - SERPAPI
    - TAVILY
    - BING SEARCH API

    This implementation uses a generic HTTP adapter pattern.
    """

    def __init__(self):
        self.provider = os.getenv("WEB_SEARCH_PROVIDER", "serpapi")
        self.api_key = os.getenv("WEB_SEARCH_API_KEY", "")
        self.endpoint = os.getenv("WEB_SEARCH_ENDPOINT", "")

    def search(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        provider = self.provider.lower()

        if provider == "serpapi":
            return self._serpapi(query, top_k)
        elif provider == "tavily":
            return self._tavily(query, top_k)
        elif provider == "bing":
            return self._bing(query, top_k)
        else:
            return self._custom(query, top_k)

    def _serpapi(self, query: str, top_k: int) -> Dict[str, Any]:
        url = "https://serpapi.com/search.json"
        params = {
            "q": query,
            "api_key": self.api_key,
            "num": top_k
        }
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        results = []
        for item in data.get("organic_results", [])[:top_k]:
            results.append({
                "title": item.get("title"),
                "snippet": item.get("snippet"),
                "url": item.get("link")
            })

        return {"query": query, "results": results, "source": "serpapi"}

    def _tavily(self, query: str, top_k: int) -> Dict[str, Any]:
        url = "https://api.tavily.com/search"
        payload = {
            "api_key": self.api_key,
            "query": query,
            "max_results": top_k
        }
        res = requests.post(url, json=payload, timeout=10)
        data = res.json()

        results = []
        for item in data.get("results", [])[:top_k]:
            results.append({
                "title": item.get("title"),
                "snippet": item.get("content"),
                "url": item.get("url")
            })

        return {"query": query, "results": results, "source": "tavily"}

    def _bing(self, query: str, top_k: int) -> Dict[str, Any]:
        url = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": query, "count": top_k}

        res = requests.get(url, headers=headers, params=params, timeout=10)
        data = res.json()

        results = []
        for item in data.get("webPages", {}).get("value", [])[:top_k]:
            results.append({
                "title": item.get("name"),
                "snippet": item.get("snippet"),
                "url": item.get("url")
            })

        return {"query": query, "results": results, "source": "bing"}

    def _custom(self, query: str, top_k: int) -> Dict[str, Any]:
        if not self.endpoint:
            return {
                "query": query,
                "results": [],
                "error": "No valid search provider configured"
            }

        res = requests.get(
            self.endpoint,
            params={"q": query, "top_k": top_k},
            timeout=10
        )

        return {"query": query, "results": res.json(), "source": "custom"}