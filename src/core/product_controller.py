# DramaFlow Studio v4 - Product Controller (Final Integration Layer)
# Bridges SearchFacade + RecommendationEngine for full product experience

from typing import Dict, Any

from src.core.search_facade import SearchFacade
from src.core.recommendation_engine import RecommendationEngine


class ProductController:
    """
    Final orchestration layer for AI product experience.

    Combines:
    - Search (AI + cache + rank)
    - History (via facade)
    - Recommendations (next-step suggestions)

    UI should prefer this layer for full product experience.
    """

    def __init__(self, config: Dict[str, Any]):
        self.facade = SearchFacade(config)
        self.recommender = RecommendationEngine()

    def search(self, query: str, limit: int = 10, debug: bool = False) -> Dict[str, Any]:
        """
        Returns full product payload:
        - results
        - history
        - recommendations
        """

        results = self.facade.search(query, limit=limit, debug=debug)
        history = self.facade.get_history()

        recommendations = self.recommender.build_suggestions(history, limit=5)

        return {
            "results": results,
            "history": history,
            "recommendations": recommendations
        }

    def clear_cache(self):
        self.facade.clear_cache()

    def get_history(self):
        return self.facade.get_history()

    def get_recommendations(self):
        history = self.facade.get_history()
        return self.recommender.build_suggestions(history, limit=5)
