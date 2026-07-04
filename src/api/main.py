# 🚀 Production API Layer (FastAPI)
# Entry point for deploying the AI Runtime as a service

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Optional

from src.domain.orchestrator.agent_orchestrator import AgentOrchestrator


# -----------------------------
# 🧠 Request Schema
# -----------------------------
class RunRequest(BaseModel):
    goal: str
    mode: Optional[str] = "auto"


# -----------------------------
# 📦 Response Schema (Product Grade)
# -----------------------------
class RunResponse(BaseModel):
    goal: str
    mode: str
    answer: Any
    plan: Any
    route: Any
    reflection: Any
    memory_size: int


# -----------------------------
# 🚀 App Init
# -----------------------------
app = FastAPI(title="DramaFlow AI Runtime", version="1.0.0")

# ⚠️ In production, use DI container
orchestrator = AgentOrchestrator(tools=None)


# -----------------------------
# 🧭 Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------------
# 🚀 Main Execution Endpoint
# -----------------------------
@app.post("/run", response_model=RunResponse)
def run(request: RunRequest):
    """
    Main entry for AI execution
    """
    result = orchestrator.run(request.goal, mode=request.mode)

    return RunResponse(
        goal=result.get("goal"),
        mode=result.get("mode"),
        answer=result.get("result"),
        plan=result.get("plan"),
        route=result.get("route"),
        reflection=result.get("reflection"),
        memory_size=result.get("memory_size", 0)
    )