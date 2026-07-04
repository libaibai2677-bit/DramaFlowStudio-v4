# 🚀 Software Entry Point (AI Runtime Application)
# This file turns the AI Runtime Kernel into a runnable software product

from fastapi import FastAPI
from pydantic import BaseModel

from src.core.bootstrap import container
from src.core.observability import Observability


# -----------------------------
# 🌐 App Initialization
# -----------------------------
app = FastAPI(title="DramaFlow AI Runtime", version="1.0.0")

orchestrator = container.get_orchestrator()


# -----------------------------
# 📦 Request Schema
# -----------------------------
class RunRequest(BaseModel):
    goal: str
    mode: str = "auto"
    tenant_id: str | None = None
    user_id: str | None = None


# -----------------------------
# ❤️ Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "DramaFlow AI Runtime"
    }


# -----------------------------
# 🚀 Main AI Endpoint
# -----------------------------
@app.post("/run")
def run(req: RunRequest):
    with Observability.span("api.request", {
        "goal": req.goal,
        "mode": req.mode
    }):
        
        Observability.start_trace()
        
        result = orchestrator.run({
            "goal": req.goal,
            "mode": req.mode,
            "tenant_id": req.tenant_id,
            "user_id": req.user_id
        })
        
        return {
            "result": result,
            "trace": Observability.get_context()
        }


# -----------------------------
# 🧪 Local Run (software mode)
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.app_entry:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )