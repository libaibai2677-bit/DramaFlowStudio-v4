# ⚡ ChatGPT-Level Real-Time Interaction Layer (WebSocket)
# Enables bidirectional streaming, interrupt, and thinking states

import json
import asyncio
from fastapi import WebSocket, WebSocketDisconnect

from src.core.bootstrap import container
from src.core.observability import Observability

orchestrator = container.get_orchestrator()

# -----------------------------
# 🧠 Connection Manager
# -----------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[id(websocket)] = websocket

    def disconnect(self, websocket: WebSocket):
        self.active_connections.pop(id(websocket), None)

    async def send(self, websocket: WebSocket, message: dict):
        await websocket.send_text(json.dumps(message))


manager = ConnectionManager()

# -----------------------------
# 🚀 WebSocket Endpoint (ChatGPT-style)
# -----------------------------
async def agent_socket(websocket: WebSocket):
    await manager.connect(websocket)

    trace_id = None
    cancelled = False

    try:
        while True:
            payload = await websocket.receive_text()
            data = json.loads(payload)

            if data.get("type") == "cancel":
                cancelled = True
                await manager.send(websocket, {"stage": "cancelled"})
                continue

            goal = data.get("goal")
            mode = data.get("mode", "auto")

            # 🧠 Thinking State
            await manager.send(websocket, {
                "stage": "thinking",
                "message": "Agent is planning..."
            })

            trace_id = Observability.start_trace()

            # ⚙️ Execution Phase
            result = orchestrator.run({
                "goal": goal,
                "mode": mode,
                "stream": True
            })

            output = str(result)

            # ⚡ Token Streaming
            buffer = ""
            for ch in output:
                if cancelled:
                    break

                buffer += ch

                await manager.send(websocket, {
                    "stage": "token",
                    "token": ch
                })

                await asyncio.sleep(0.01)

            # 🏁 Done State
            if not cancelled:
                await manager.send(websocket, {
                    "stage": "done",
                    "trace_id": trace_id,
                    "final": buffer
                })

    except WebSocketDisconnect:
        manager.disconnect(websocket)