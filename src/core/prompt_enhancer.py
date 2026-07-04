# DramaFlow Studio v4 - AI Prompt Enhancement Layer (Phase 4)
# Converts user input into richer search intents

from typing import Dict, Any


class PromptEnhancer:
    """
    Lightweight AI-like prompt enhancer.

    Goal:
    - Expand short queries into richer visual search prompts
    - Improve image retrieval quality
    - Prepare for future NLP/LLM integration
    """

    def __init__(self):
        # Simple style presets (MVP heuristic)
        self.style_tags = {
            "default": ["high quality", "detailed", "sharp focus"],
            "portrait": ["portrait", "soft lighting", "bokeh"],
            "landscape": ["wide angle", "natural light", "4k"],
            "night": ["night scene", "low light", "cinematic"],
        }

    def detect_intent(self, query: str) -> str:
        q = query.lower()

        if any(k in q for k in ["person", "girl", "man", "portrait"]):
            return "portrait"
        if any(k in q for k in ["mountain", "sea", "city", "forest"]):
            return "landscape"
        if any(k in q for k in ["night", "dark", "neon"]):
            return "night"
        return "default"

    def enhance(self, query: str) -> str:
        """
        Expand user query into richer visual prompt.
        """

        intent = self.detect_intent(query)
        tags = self.style_tags.get(intent, self.style_tags["default"])

        enhanced = f"{query}, {', '.join(tags)}"

        return enhanced

    def enrich_payload(self, query: str) -> Dict[str, Any]:
        """
        Return structured AI-enhanced query object.
        """
        return {
            "original": query,
            "enhanced": self.enhance(query),
            "intent": self.detect_intent(query)
        }
}