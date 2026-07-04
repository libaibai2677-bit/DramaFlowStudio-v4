# DramaFlow Studio v4 - AI Pipeline Engine V3 (Phase 4)
# End-to-end wiring: PromptEnhancer → SmartEngineV2 → Cache → Ranker

from typing import List, Dict, Any

from src.core.prompt_enhancer import PromptEnhancer
from src.image_search.engine_smart_v2 import SmartImageSearchEngineV2


class AIImageSearchEngineV3:
    """
    Full AI pipeline engine.

    This version wires together:
    - Prompt Enhancement (intent + expansion)
    - Smart Engine V2 (cache + ranking)
    - Unified AI-style search entry point
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config

        self.enhancer = PromptEnhancer()
        self.smart_engine = SmartImageSearchEngineV2(config)

    def search(self, query: str, limit: int = 10, debug: bool = False) -> List[Dict[str, Any]]:
        """
        AI-powered search pipeline:

        1. Analyze & enhance prompt
        2. Run smart engine search
        3. Return ranked results
        """

        enriched = self.enhancer.enrich_payload(query)
        enhanced_query = enriched["enhanced"]

        if debug:
            print("[AI PIPELINE]")
            print(f"Original: {enriched['original']}")
            print(f"Enhanced: {enriched['enhanced']}")
            print(f"Intent: {enriched['intent']}")

        results = self.smart_engine.search(enhanced_query, limit=limit)

        # Attach AI metadata to results
        for item in results:
            item["ai_intent"] = enriched["intent"]
            item["ai_query"] = enriched["enhanced"]

        return results

    def clear_cache(self):
        self.smart_engine.clear_cache()
