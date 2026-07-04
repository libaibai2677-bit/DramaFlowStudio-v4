# DramaFlow Studio v4 — Hardening Phase
# Normalizer Layer (Critical Contract Enforcement)
# Converts UnifiedEngine raw output → EngineResponseDTO

from typing import Dict, Any, List
from src.core.dto import SearchResultDTO, EngineResponseDTO


class ResultNormalizer:
    """
    Ensures ALL engine outputs conform to a strict schema.
    This prevents UI/service layer fragmentation.
    """

    def normalize(self, raw: Dict[str, Any]) -> EngineResponseDTO:
        """
        Normalize raw engine output into EngineResponseDTO
        """

        enhanced_query = raw.get("enhanced_query", "")
        intent = raw.get("intent", "default")
        results_raw = raw.get("results", [])

        results: List[SearchResultDTO] = []

        for i, r in enumerate(results_raw):
            if isinstance(r, dict):
                results.append(
                    SearchResultDTO(
                        id=str(r.get("id", i)),
                        title=r.get("title", "Untitled"),
                        image_url=r.get("image") or r.get("image_url"),
                        score=float(r.get("score", 0.0)),
                        tags=r.get("tags", []) or [],
                        explanation=r.get("explanation"),
                        metadata=r.get("metadata", {})
                    )
                )
            else:
                results.append(
                    SearchResultDTO(
                        id=str(i),
                        title=str(r),
                        score=0.0,
                        tags=[]
                    )
                )

        return EngineResponseDTO(
            enhanced_query=enhanced_query,
            intent=intent,
            results=results,
            raw=raw
        )