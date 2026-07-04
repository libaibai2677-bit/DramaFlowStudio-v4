# DramaFlow Studio v4 - Unified Core Engine (Phase 6 Refactor)
# Production-grade single pipeline core (replaces Facade + AI Engine duplication)

from typing import List, Dict, Any

from src.core.prompt_enhancer import PromptEnhancer
from src.core.cache import SimpleCache
from src.core.ranker import ImageRanker
from src.core.history_manager import HistoryManager
from src.core.recommendation_engine import RecommendationEngine
from src.image_search.engine import ImageSearchEngine


class UnifiedEngine:
    """
    SINGLE source of truth for AI image search system.

    This replaces:
    - SearchFacade
    - AIImageSearchEngineV3

    Responsibilities:
    - Prompt understanding
    - Search execution
    - Ranking
    - Cache
    - History
    - Recommendations
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config

        self.engine = ImageSearchEngine(config)

        self.enhancer = PromptEnhancer()
        self.cache = SimpleCache()
        self.ranker = ImageRanker()

        self.history = HistoryManager()
        self.recommender = RecommendationEngine()

    def search(self, query: str, limit: int = 10, debug: bool = False) -> Dict[str, Any]:
        """
        End-to-end unified AI pipeline.
        """

        enriched = self.enhancer.enrich_payload(query)
        enhanced_query = enriched["enhanced"]
        intent = enriched["intent"]

        cache_key = f"unified:{enhanced_query}:{limit}"

        cached = self.cache.get(cache_key)
        if cached:
            history = self.history.list()
            recommendations = self.recommender.build_suggestions(history)

            return {
                "query": query,
                "enhanced_query": enhanced_query,
                "intent": intent,
                "results": cached,
                "cached": True,
                "history": history,
                "recommendations": recommendations,
            }

        results = self.engine.search(enhanced_query, limit=limit * 2)

        try:
            ranked = self.ranker.rank(results)
        except Exception:
            ranked = results

        final_results = ranked[:limit]

        self.cache.set(cache_key, final_results, ttl=300)

        self.history.add(query, enhanced_query, intent, final_results)

        history = self.history.list()
        recommendations = self.recommender.build_suggestions(history)

        return {
            "query": query,
            "enhanced_query": enhanced_query,
            "intent": intent,
            "results": final_results,
            "cached": False,
            "history": history,
            "recommendations": recommendations,
        }

    def clear_cache(self):
        self.cache.clear()

    def reset_history(self):
        self.history.clear()
