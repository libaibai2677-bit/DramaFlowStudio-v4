# DramaFlow Studio v4 - Smart Engine V2 (Phase 3)
# Integrates Cache + Ranking into a unified search pipeline

from typing import List, Dict, Any

from src.core.cache import SimpleCache
from src.core.ranker import ImageRanker
from src.image_search.engine import ImageSearchEngine


class SmartImageSearchEngineV2:
    """
    Enhanced image search engine with:

    - Caching layer
    - Smart ranking layer
    - Drop-in replacement for base engine
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config

        self.base_engine = ImageSearchEngine(config)
        self.cache = SimpleCache()
        self.ranker = ImageRanker()

    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Smart search pipeline:
        1. Check cache
        2. Fetch from base engine if needed
        3. Rank results
        4. Store cache
        """

        cache_key = f"search:{query}:{limit}"

        cached = self.cache.get(cache_key)
        if cached:
            return cached

        results = self.base_engine.search(query, limit=limit * 2)

        if not results:
            return []

        try:
            ranked = self.ranker.rank(results)
        except Exception:
            ranked = results

        final_results = ranked[:limit]

        self.cache.set(cache_key, final_results, ttl=300)

        return final_results

    def clear_cache(self):
        self.cache.clear()
