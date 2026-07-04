# 🧭 Agent Orchestrator (Unified Runtime Entry Layer)
# This is the single entry point for the entire AI system

from typing import Dict, Any

from src.domain.agents.planner import Planner
from src.domain.agents.agent_loop import AgentLoop
from src.domain.agents.reflection import ReflectionEngine
from src.domain.agents.self_improvement_loop import SelfImprovementLoop
from src.domain.agents.multi_agent_system import MultiAgentSystem
from src.domain.agents.agent_mesh import AgentMesh
from src.domain.agents.tool_router import ToolRouter
from src.domain.memory.memory_store import MemoryStore


class AgentOrchestrator:
    """
    🧠 Unified AI Runtime Controller

    This is the SINGLE entry point for the system.

    Responsibilities:
    - interpret goal
    - select execution mode
    - coordinate agents
    - manage memory
    - return structured output
    """

    def __init__(self, tools: Any):
        self.tools = tools

        self.planner = Planner()
        self.reflection = ReflectionEngine()
        self.memory = MemoryStore()
        self.tool_router = ToolRouter(tools)

        self.agent_loop = AgentLoop(tools)
        self.multi_agent = MultiAgentSystem(tools)
        self.mesh = AgentMesh(tools)
        self.self_improve = SelfImprovementLoop(tools)

    def run(self, goal: str, mode: str = "auto") -> Dict[str, Any]:
        """
        Main execution entry
        Modes:
        - auto: system decides best strategy
        - single: single agent execution
        - multi: multi-agent collaboration
        - mesh: swarm execution
        - evolve: self-improving loop
        """

        # 🧠 Store incoming request
        self.memory.save("goal_received", {"goal": goal, "mode": mode})

        # 🧭 Plan
        plan = self.planner.create_plan(goal)

        # 🧠 Route tools (light decision layer)
        route = self.tool_router.route(goal)

        result = None

        # 🔁 Mode selection
        if mode == "single":
            result = self.agent_loop.run(goal)

        elif mode == "multi":
            result = self.multi_agent.run(goal)

        elif mode == "mesh":
            node = self.mesh.spawn_node()
            result = node.run(goal)

        elif mode == "evolve":
            result = self.self_improve.run(goal)

        else:
            # auto mode (simple heuristic)
            if "complex" in goal.lower() or "compare" in goal.lower():
                result = self.multi_agent.run(goal)
            elif "optimize" in goal.lower() or "improve" in goal.lower():
                result = self.self_improve.run(goal)
            else:
                result = self.agent_loop.run(goal)

        # 🪞 Reflection
        reflection = self.reflection.evaluate(goal, result)

        # 🧠 Store experience
        self.memory.save("execution", {
            "goal": goal,
            "plan": plan,
            "route": route,
            "result": result,
            "reflection": reflection
        })

        # 📦 Unified Output Schema (PRODUCT GRADE)
        return {
            "goal": goal,
            "mode": mode,
            "plan": plan,
            "route": route,
            "result": result,
            "reflection": reflection,
            "memory_size": len(self.memory.all())
        }