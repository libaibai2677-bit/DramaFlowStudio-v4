# DramaFlow Studio v4 - Search Facade (Phase 5 Core Unification Layer)
# Single entry point for UI → AI Image Search System

from typing import List, Dict, Any

from src.core.prompt_enhancer import PromptEnhancer
from src.core.cache import SimpleCache
from src.core.ranker import ImageRanker
from src.core.history_manager import HistoryManager
from src.image_search.engine import ImageSearchEngine


class SearchFacade:
    """
    Unified entry point for DramaFlow Studio v4.

    Responsibilities:
    - Prompt enhancement (AI intent)
    - Cache management
    - Ranking
    - History tracking
    - Provider search orchestration

    UI MUST ONLY CALL THIS CLASS.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config

        self.engine = ImageSearchEngine(config)
        self.enhancer = PromptEnhancer()
        self.cache = SimpleCache()
        self.ranker = ImageRanker()
        self.history = HistoryManager()

    def search(self, query: str, limit: int = 10, debug: bool = False) -> List[Dict[str, Any]]:
        enriched = self.enhancer.enrich_payload(query)
        enhanced_query = enriched["enhanced"]
        intent = enriched["intent"]

        cache_key = f"facade:{enhanced_query}:{limit}"

        cached = self.cache.get(cache_key)
        if cached:
            self.history.add(query, enhanced_query, intent, cached)
            return cached

        results = self.engine.search(enhanced_query, limit=limit * 2)

        if not results:
            self.history.add(query, enhanced_query, intent, [])
            return []

        try:
            ranked = self.ranker.rank(results)
        except Exception:
            ranked = results

        final_results = ranked[:limit]

        self.cache.set(cache_key, final_results, ttl=300)
        self.history.add(query, enhanced_query, intent, final_results)

        if debug:
            print("[SearchFacade]")
            print(f"query: {query}")
            print(f"enhanced: {enhanced_query}")
            print(f"intent: {intent}")
            print(f"results: {len(final_results)}")

        return final_results

    def clear_cache(self):
        self.cache.clear()

    def get_history(self):
        return self.history.list()
