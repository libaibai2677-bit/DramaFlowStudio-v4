# ⚡ Token-Level Streaming Layer (SSE)
# Enables real-time AI output streaming for UI

import time
import json
from fastapi import Request
from fastapi.responses import StreamingResponse

from src.core.bootstrap import container
from src.core.observability import Observability

orchestrator = container.get_orchestrator()

# -----------------------------
# 🚀 Streaming Generator
# -----------------------------
def generate_stream(payload: dict):
    goal = payload.get("goal")
    mode = payload.get("mode", "auto")

    trace_id = Observability.start_trace()

    # Step 1: planning phase
    yield f"data: {json.dumps({'stage': 'planning'})}\n\n"
    time.sleep(0.3)

    # Step 2: simulate token streaming from orchestrator
    result = orchestrator.run({
        "goal": goal,
        "mode": mode,
        "stream": True
    })

    # Simulate token-level output (replace with real LLM stream later)
    output = str(result)

    # emit token-level SSE stream
    for ch in output:
        yield f"data: {json.dumps({'token': ch})}\n\n"
        time.sleep(0.01)

    # Step 3: final payload
    yield f"data: {json.dumps({'stage': 'done', 'trace_id': trace_id})}\n\n"


# -----------------------------
# 🌍 Streaming Endpoint
# -----------------------------
def run_stream(request: Request, payload: dict):
    return StreamingResponse(
        generate_stream(payload),
        media_type="text/event-stream"
    )