# 🧠 Memory System (Long-Term Context Layer)
# Adds persistence + experience storage for Agent evolution

from typing import List, Dict, Any
import json


class MemoryStore:
    """
    Simple long-term memory for Agent system.
    Stores past interactions, outcomes, and insights.
    """

    def __init__(self):
        self.memories: List[Dict[str, Any]] = []

    def save(self, event_type: str, content: Dict[str, Any]):
        self.memories.append({
            "type": event_type,
            "content": content
        })

    def retrieve(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        results = []
        for m in self.memories:
            if query.lower() in json.dumps(m).lower():
                results.append(m)
        return results[:limit]

    def all(self) -> List[Dict[str, Any]]:
        return self.memories