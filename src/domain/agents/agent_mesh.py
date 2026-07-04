# 🌐 Agent Mesh System (Swarm Intelligence Layer)
# Final evolution: decentralized coordination across multiple agent groups

from typing import Dict, Any, List

from src.domain.agents.multi_agent_system import MultiAgentSystem


class AgentMesh:
    """
    A lightweight swarm-style coordination layer.
    Multiple Multi-Agent Systems collaborate on complex goals.
    """

    def __init__(self, tools):
        self.tools = tools
        self.nodes: List[MultiAgentSystem] = []

    def spawn_node(self) -> MultiAgentSystem:
        node = MultiAgentSystem(self.tools)
        self.nodes.append(node)
        return node

    def broadcast(self, goal: str) -> List[Dict[str, Any]]:
        """
        Send goal to all agent nodes and collect results.
        """
        results = []

        for node in self.nodes:
            result = node.run(goal)
            results.append(result)

        return results

    def consensus(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Very simple consensus mechanism:
        picks first successful result.
        (Upgradeable to voting / ranking later)
        """
        for r in results:
            if r.get("final_output"):
                return r

        return {"status": "no_consensus", "results": results}