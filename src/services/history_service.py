# DramaFlow Studio v4 - History Service (Phase 7 Refactor)
# Clean service layer extraction from monolithic engine design

from typing import List, Dict, Any


class HistoryService:
    """
    Dedicated service for managing user search history.

    This replaces embedded history logic inside:
    - UnifiedEngine
    - ProductController (future cleanup target)
    - SearchFacade (deprecated)

    Goal:
    - Single responsibility
    - Reusable across product layers
    - Easier testing & persistence upgrade
    """

    def __init__(self):
        self._history: List[Dict[str, Any]] = []

    def add(self, query: str, enhanced_query: str, intent: str, results: List[Dict[str, Any]]):
        self._history.append({
            "query": query,
            "enhanced_query": enhanced_query,
            "intent": intent,
            "results_count": len(results)
        })

    def list(self) -> List[Dict[str, Any]]:
        return list(self._history)

    def clear(self):
        self._history.clear()

    def last(self, n: int = 10) -> List[Dict[str, Any]]:
        return self._history[-n:]
