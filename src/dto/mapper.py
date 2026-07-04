class ResultDTO:
    def __init__(self, enhanced_query, intent, results):
        self.enhanced_query = enhanced_query
        self.intent = intent
        self.results = results

class ResultMapper:
    @staticmethod
    def to_dto(data):
        return ResultDTO(
            data.get("enhanced_query", ""),
            data.get("intent", "unknown"),
            data.get("results", []),
        )