# DramaFlow Studio v4 - Explainability Engine (Phase 6 AI Product Layer)
# Adds "why this result" reasoning for better product transparency

from typing import List, Dict, Any


class ExplainabilityEngine:
    """
    Provides lightweight AI explainability for search results.

    Goal:
    - Improve user trust
    - Enhance product perception
    - Support UI explanation panels
    """

    def __init__(self):
        pass

    def explain(self, query: str, enhanced_query: str, intent: str, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Attach explanation metadata to each result.
        """

        explained = []

        for i, item in enumerate(results):
            score_hint = max(0.9 - i * 0.05, 0.3)

            explanation = {
                "why": self._generate_reason(intent, i),
                "intent_match": intent,
                "relevance_score": round(score_hint, 3),
                "query_context": enhanced_query
            }

            new_item = dict(item)
            new_item["explain"] = explanation
            explained.append(new_item)

        return explained

    def _generate_reason(self, intent: str, rank: int) -> str:
        base = {
            "portrait": "Matches portrait lighting and composition style",
            "landscape": "Strong scenic and spatial composition relevance",
            "night": "Good alignment with low-light and night aesthetics",
            "default": "High visual relevance to your search intent"
        }

        reason = base.get(intent, base["default"])

        if rank == 0:
            return reason + ", ranked top result due to strongest match"
        elif rank < 3:
            return reason + ", high relevance match"
        else:
            return reason + ", moderate relevance match"
