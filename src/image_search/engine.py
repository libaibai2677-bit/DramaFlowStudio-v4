# DramaFlow Studio v4 - Image Search Engine MVP

from typing import List, Dict, Any
from src.image_search.providers.pexels import PexelsProvider


class ImageSearchEngine:
    """
    MVP Image Search Engine
    Currently supports only Pexels provider.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.pexels = PexelsProvider(config)

    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search images from available providers.
        """
        results = []

        if self.config.get("providers", {}).get("pexels", {}).get("enabled", True):
            results.extend(self.pexels.search(query, limit))

        # Future: merge + rank results
        return results[:limit]
