# 🧠🤝 Multi-Agent System (Collaboration Layer)
# Final evolution: multiple specialized agents working together

from typing import Dict, Any, List

from src.domain.agents.agent_loop import AgentLoop
from src.domain.agents.planner import Planner
from src.domain.agents.reflection import ReflectionEngine


class AgentRole:
    PLANNER = "planner"
    EXECUTOR = "executor"
    CRITIC = "critic"


class MultiAgentSystem:
    """
    Coordinates multiple agents with different responsibilities:
    - Planner Agent
    - Executor Agent
    - Critic (Reflection) Agent
    """

    def __init__(self, tools):
        self.tools = tools

        self.planner = Planner()
        self.executor = AgentLoop(tools)
        self.critic = ReflectionEngine()

    def run(self, goal: str) -> Dict[str, Any]:

        state = {
            "goal": goal,
            "plan": None,
            "execution": None,
            "critique": None,
            "final_output": None
        }

        # 🧭 PLANNING AGENT
        plan = self.planner.create_plan(goal)
        state["plan"] = plan

        # 🤖 EXECUTION AGENT
        execution_result = self.executor.run(goal)
        state["execution"] = execution_result

        # 🪞 CRITIC AGENT
        critique = self.critic.evaluate(goal, execution_result)
        state["critique"] = critique

        # 🔄 FINAL DECISION LOGIC
        if critique["needs_improvement"]:
            state["final_output"] = {
                "status": "needs_revision",
                "reason": critique["feedback"],
                "suggestion": "re-run with improved plan"
            }
        else:
            state["final_output"] = execution_result

        return state