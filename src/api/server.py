# DramaFlow Studio v4 — SaaS Phase
# FastAPI Backend Layer (Productization for external API access)

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional

from src.core.product_controller import ProductController


app = FastAPI(title="DramaFlow Studio API", version="v4-saas")

controller = ProductController()


# -----------------------------
# Simple API Key Auth (MVP SaaS Layer)
# -----------------------------
API_KEY = "demo-key-change-me"


def verify_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


# -----------------------------
# Request / Response Models
# -----------------------------
class SearchRequest(BaseModel):
    query: str


class SearchResponse(BaseModel):
    enhanced_query: str
    intent: str
    results: list


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok", "service": "dramaflow-v4-saas"}


# -----------------------------
# Core SaaS Endpoint
# -----------------------------
@app.post("/search", response_model=SearchResponse)
def search(req: SearchRequest, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)

    try:
        result = controller.search(req.query)

        return {
            "enhanced_query": result.enhanced_query,
            "intent": result.intent,
            "results": [r.__dict__ for r in result.results]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
