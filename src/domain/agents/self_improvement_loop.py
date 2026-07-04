# 🔄 Self-Improvement Loop (Adaptive Agent Evolution Layer)
# Connects Reflection → Planning → Execution for continuous improvement

from typing import Dict, Any

from src.domain.agents.reflection import ReflectionEngine
from src.domain.agents.planner import Planner
from src.domain.agents.agent_loop import AgentLoop
from src.domain.memory.memory_store import MemoryStore


class SelfImprovementLoop:
    """
    Final evolutionary layer:
    runs agent → evaluates → adapts → re-plans
    """

    def __init__(self, tools):
        self.reflection = ReflectionEngine()
        self.planner = Planner()
        self.agent = AgentLoop(tools)
        self.memory = MemoryStore()

    def run(self, goal: str, iterations: int = 2) -> Dict[str, Any]:
        state = {
            "goal": goal,
            "iterations": [],
            "final_output": None
        }

        current_goal = goal

        for i in range(iterations):

            # 🧭 PLAN
            plan = self.planner.create_plan(current_goal)

            # 🔁 EXECUTE (Agent)
            result = self.agent.run(current_goal)

            # 🪞 REFLECT
            reflection = self.reflection.evaluate(current_goal, result)

            # 🧠 STORE EXPERIENCE
            self.memory.save("iteration", {
                "goal": current_goal,
                "plan": plan,
                "result": result,
                "reflection": reflection
            })

            state["iterations"].append({
                "plan": plan,
                "result": result,
                "reflection": reflection
            })

            # 🔄 ADAPTATION LOGIC
            if reflection["needs_improvement"]:
                current_goal = f"Improve previous attempt: {current_goal}"
            else:
                break

            state["final_output"] = result

        return state