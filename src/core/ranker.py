# DramaFlow Studio v4 - Smart Ranking Layer (Phase 3)
# Provides basic image quality scoring for search results

from typing import List, Dict, Any


class ImageRanker:
    """
    Simple heuristic-based image ranking engine (MVP smart layer).

    Goal:
    - Improve result ordering before UI display
    - Provide foundation for future AI-based ranking
    """

    def __init__(self, provider_weights: Dict[str, float] = None):
        # Default provider preference weights
        self.provider_weights = provider_weights or {
            "pexels": 1.0,
            "unsplash": 1.1,
            "pixabay": 0.9
        }

    def score(self, item: Dict[str, Any]) -> float:
        """
        Compute a simple heuristic score for an image item.
        """
        score = 0.0

        # 1. Provider weight
        provider = item.get("source", "")
        score += self.provider_weights.get(provider, 1.0)

        # 2. Has title (alt text quality)
        title = item.get("title", "")
        if title and len(title) > 10:
            score += 0.5
        elif title:
            score += 0.2

        # 3. Has thumbnail
        if item.get("thumbnail"):
            score += 0.3

        # 4. Has full URL
        if item.get("url"):
            score += 0.5

        return score

    def rank(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Return items sorted by score (descending).
        """
        scored = []

        for item in items:
            item_copy = dict(item)
            item_copy["_score"] = self.score(item)
            scored.append(item_copy)

        scored.sort(key=lambda x: x["_score"], reverse=True)

        # Remove internal score before returning
        for item in scored:
            item.pop("_score", None)

        return scored
