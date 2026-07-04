# DramaFlow Studio v4 — Hardening Phase
# Data Transfer Objects (DTO Layer)
# This enforces a strict contract between AI Engine → Services → UI

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class SearchResultDTO:
    """
    Unified output contract for all AI search results.
    All engine outputs MUST be normalized into this structure.
    """
    id: str
    title: str
    image_url: Optional[str] = None

    score: float = 0.0
    tags: List[str] = field(default_factory=list)

    explanation: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EngineResponseDTO:
    """
    Standard response from UnifiedEngine.
    This prevents UI/service layer from depending on raw dicts.
    """
    enhanced_query: str
    intent: str
    results: List[SearchResultDTO]

    raw: Dict[str, Any] = field(default_factory=dict)
