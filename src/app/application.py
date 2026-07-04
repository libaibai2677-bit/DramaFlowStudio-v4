# DramaFlow Studio v4 - Application Layer
# This layer decouples UI from business logic

from typing import Dict, Any, List
from src.image_search.engine import ImageSearchEngine
from src.core.logger import get_logger


class Application:
    """
    Central application controller.
    Acts as a bridge between UI and core engines.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = get_logger(__name__)
        self.image_engine = ImageSearchEngine(config)

        self.logger.info("Application layer initialized")

    def search_images(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Unified entry for image search.
        UI should ONLY call this method.
        """
        self.logger.info(f"Searching images: {query}")

        results = self.image_engine.search(query, limit=limit)

        self.logger.info(f"Found {len(results)} results")
        return results

    def get_config(self) -> Dict[str, Any]:
        return self.config
