# DramaFlow Studio v4 - History Manager (Phase 5: Productization)
# Adds memory of searches, results, and AI context

from typing import List, Dict, Any
import time


class HistoryItem:
    def __init__(self, query: str, enhanced_query: str, intent: str, results: List[Dict[str, Any]]):
        self.query = query
        self.enhanced_query = enhanced_query
        self.intent = intent
        self.results = results
        self.timestamp = time.time()


class HistoryManager:
    """
    Stores user search history + AI context.

    Phase 5 goal:
    - Enable recents panel
    - Enable future recommendation system
    - Provide UX continuity
    """

    def __init__(self, max_items: int = 50):
        self.max_items = max_items
        self._items: List[HistoryItem] = []

    def add(self, query: str, enhanced_query: str, intent: str, results: List[Dict[str, Any]]):
        item = HistoryItem(query, enhanced_query, intent, results)
        self._items.insert(0, item)

        if len(self._items) > self.max_items:
            self._items = self._items[: self.max_items]

    def list(self) -> List[Dict[str, Any]]:
        return [
            {
                "query": i.query,
                "enhanced_query": i.enhanced_query,
                "intent": i.intent,
                "timestamp": i.timestamp,
                "result_count": len(i.results),
            }
            for i in self._items
        ]

    def clear(self):
        self._items.clear()
