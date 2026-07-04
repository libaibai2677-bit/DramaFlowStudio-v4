# 🔁 Agent Loop (Autonomous Execution Core)
# Evolves system from Tool-Calling → Agent Behavior

from typing import Any, Dict

from src.domain.services.tool_registry import ToolRegistry
from src.domain.services.ai_enhanced_service import EnhancedAIEngineService


class AgentLoop:
    """
    Minimal autonomous loop:
    observe → think → decide → act

    This is the foundation for Agent-based systems.
    """

    def __init__(self, tools: ToolRegistry):
        self.tools = tools
        self.ai = EnhancedAIEngineService()

    def run(self, query: str, max_steps: int = 3) -> Dict[str, Any]:
        state = {
            "query": query,
            "steps": [],
            "final_output": None
        }

        current_input = query

        for step in range(max_steps):
            # 🧠 THINK
            ai_output = self.ai.process(current_input)

            strategy = ai_output.get("strategy")
            answer = ai_output.get("answer")

            step_record = {
                "step": step,
                "strategy": strategy,
                "answer": answer
            }

            state["steps"].append(step_record)

            # 🧩 DECIDE (simple heuristic)
            if "tool:" in current_input.lower():
                tool_name = current_input.split("tool:")[-1].strip()
                tool_result = self.tools.execute(tool_name)

                state["steps"][-1]["tool_result"] = tool_result
                state["final_output"] = tool_result
                break

            # 🔁 FEEDBACK LOOP
            current_input = answer
            state["final_output"] = answer

        return state