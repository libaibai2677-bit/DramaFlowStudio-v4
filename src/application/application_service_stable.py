# 🧠 Application Service Layer (Stabilized Internal Version)

from src.domain.services.ai_engine_service import AIEngineService
from src.dto.mapper import ResultMapper


class ApplicationService:
    """
    Single orchestration entry for internal AI platform.
    Legacy controller removed for clean architecture.
    """

    def __init__(self):
        self.ai_engine = AIEngineService()

    def execute_query(self, query: str):
        # AI processing
        ai_result = self.ai_engine.process(query)

        merged = {
            "enhanced_query": ai_result.get("enhanced_query", query),
            "intent": ai_result.get("intent", "general"),
            "results": []
        }

        return ResultMapper.to_dto(merged)
