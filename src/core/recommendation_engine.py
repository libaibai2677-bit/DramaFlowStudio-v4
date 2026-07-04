# DramaFlow Studio v4 - Recommendation Engine (Phase 5 AI Product Layer)
# Generates user-based suggestions from history + intent patterns

from typing import List, Dict, Any
from collections import Counter


class RecommendationEngine:
    """
    Lightweight recommendation system based on:

    - Search history intents
    - Frequent queries
    - Lightweight heuristic similarity

    Goal:
    Turn history into proactive suggestions.
    """

    def __init__(self):
        pass

    def _extract_intents(self, history: List[Dict[str, Any]]) -> List[str]:
        return [h.get("intent", "default") for h in history]

    def _extract_queries(self, history: List[Dict[str, Any]]) -> List[str]:
        return [h.get("query", "") for h in history]

    def build_suggestions(self, history: List[Dict[str, Any]], limit: int = 5) -> List[str]:
        """
        Generate simple recommendations based on usage patterns.
        """

        if not history:
            return [
                "city night lights",
                "portrait soft lighting",
                "minimalist architecture",
                "nature landscape 4k",
                "cinematic street photography"
            ]

        intents = self._extract_intents(history)
        intent_counts = Counter(intents)

        top_intent = intent_counts.most_common(1)[0][0]

        templates = {
            "portrait": [
                "portrait cinematic lighting",
                "soft bokeh portrait",
                "studio portrait photography",
                "natural light face portrait"
            ],
            "landscape": [
                "ultra wide landscape 4k",
                "mountain sunrise scenery",
                "forest nature cinematic",
                "aerial landscape view"
            ],
            "night": [
                "neon city night cyberpunk",
                "rainy night street lights",
                "dark cinematic atmosphere",
                "long exposure city lights"
            ],
            "default": [
                "high quality aesthetic images",
                "cinematic photography style",
                "minimal clean composition",
                "professional photography"
            ]
        }

        suggestions = templates.get(top_intent, templates["default"])

        return suggestions[:limit]
