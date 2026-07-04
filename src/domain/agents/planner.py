# 🧭 Planner Module (Goal Decomposition Layer)
# Upgrades Agent from reactive → goal-driven behavior

from typing import List, Dict, Any


class Planner:
    """
    Breaks a high-level goal into executable steps.
    This enables task decomposition for Agent systems.
    """

    def create_plan(self, goal: str) -> List[Dict[str, Any]]:
        # Simple heuristic planner (upgradeable to LLM planner later)
        steps = []

        if "analyze" in goal.lower():
            steps = [
                {"step": "understand_input", "action": "read_context"},
                {"step": "retrieve_knowledge", "action": "rag_search"},
                {"step": "generate_insight", "action": "llm_generate"}
            ]
        elif "build" in goal.lower():
            steps = [
                {"step": "requirements", "action": "clarify_goal"},
                {"step": "design", "action": "create_architecture"},
                {"step": "implement", "action": "execute_tools"}
            ]
        else:
            steps = [
                {"step": "interpret", "action": "llm_generate"},
                {"step": "respond", "action": "finalize_output"}
            ]

        return steps