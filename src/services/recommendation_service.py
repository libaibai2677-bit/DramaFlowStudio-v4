# DramaFlow Studio v4 - Recommendation Service (Phase 7 Refactor)
# Service layer wrapper for recommendation logic

from typing import List

from src.core.recommendation_engine import RecommendationEngine
from src.services.history_service import HistoryService


class RecommendationService:
    """
    Service layer abstraction over RecommendationEngine.

    Responsibilities:
    - Transform history into suggestions
    - Provide stable API for ProductController
    - Decouple product layer from core engine logic
    """

    def __init__(self, history_service: HistoryService):
        self.engine = RecommendationEngine()
        self.history_service = history_service

    def get_recommendations(self, limit: int = 5) -> List[str]:
        history = self.history_service.list()
        return self.engine.build_suggestions(history, limit=limit)

    def get_trending(self) -> List[str]:
        """Future hook for analytics-based trending"""
        return [
            "cinematic lighting portrait",
            "ultra realistic landscape",
            "cyberpunk night city",
            "minimal product photography",
            "soft natural light photography"
        ]