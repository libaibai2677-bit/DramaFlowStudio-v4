# DramaFlow Studio v4 — Hardening Phase
# Standardized Error Handling Layer
# Ensures graceful degradation across Engine → Service → UI

from typing import Optional, Dict, Any


class EngineError(Exception):
    """
    Base exception for all AI engine related failures.
    """
    pass


class NormalizationError(Exception):
    """
    Raised when raw engine output cannot be normalized into DTO.
    """
    pass


class SafeFallback:
    """
    Provides safe fallback responses when system fails.
    Prevents UI crashes and improves product stability.
    """

    @staticmethod
    def empty_result() -> Dict[str, Any]:
        return {
            "enhanced_query": "",
            "intent": "default",
            "results": [],
            "error": True,
            "message": "No results available"
        }

    @staticmethod
    def engine_failed(message: Optional[str] = None) -> Dict[str, Any]:
        return {
            "enhanced_query": "",
            "intent": "default",
            "results": [],
            "error": True,
            "message": message or "Engine failure"
        }
