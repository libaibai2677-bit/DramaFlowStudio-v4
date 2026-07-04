# 🧠 AI Engine Service (Refactored Core)
# This replaces direct AI logic inside Controller and becomes pluggable

class AIEngineService:
    """
    Lightweight AI orchestration layer.
    In production, this can be swapped with:
    - LLM API (OpenAI / local model)
    - Rule-based engine
    - Multi-model router
    """

    def process(self, query: str) -> dict:
        enhanced_query = f"[enhanced] {query}"

        if "search" in query.lower():
            intent = "search"
        elif "explain" in query.lower():
            intent = "explain"
        else:
            intent = "general"

        return {
            "enhanced_query": enhanced_query,
            "intent": intent
        }
