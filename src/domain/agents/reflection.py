# 🪞 Reflection Module (Self-Improvement Layer)
# Enables agent self-evaluation and iterative improvement

from typing import Dict, Any


class ReflectionEngine:
    """
    Evaluates agent outputs and generates improvement signals.
    This is the first step toward self-improving agents.
    """

    def evaluate(self, query: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simple heuristic reflection:
        - checks completeness
        - checks tool usage
        - checks clarity
        """

        answer = result.get("answer", "")
        strategy = result.get("strategy", "")

        score = 0
        feedback = []

        # completeness check
        if len(answer) > 50:
            score += 1
        else:
            feedback.append("Answer may be too short")

        # strategy usage check
        if strategy in ["smart", "balanced", "fast"]:
            score += 1
        else:
            feedback.append("Missing valid strategy")

        # query alignment check
        if any(word in answer.lower() for word in query.lower().split()):
            score += 1
        else:
            feedback.append("Low query alignment")

        return {
            "score": score,
            "max_score": 3,
            "feedback": feedback,
            "needs_improvement": score < 2
        }
