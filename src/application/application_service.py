# Application Service Layer (Core Orchestration)
from src.core.product_controller import ProductController
from src.dto.mapper import ResultMapper
from src.domain.services.ai_engine_service import AIEngineService

class ApplicationService:
    def __init__(self):
        self.ai_engine = AIEngineService()
        self.controller = ProductController()

    def execute_query(self, query: str):
        ai_result = self.ai_engine.process(query)
        legacy_result = self.controller.search(query)

        merged = {
            "enhanced_query": ai_result.get("enhanced_query", query),
            "intent": ai_result.get("intent", "unknown"),
            "results": legacy_result.results,
        }

        return ResultMapper.to_dto(merged)
