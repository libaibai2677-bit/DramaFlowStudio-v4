# Production Hardening Layer
# Observability + Security + Reliability

import time
import uuid
import json
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("dramaflow")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)


def log_json(event, **kwargs):
    logger.info(json.dumps({"event": event, "ts": time.time(), **kwargs}))


class ObservabilityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        rid = str(uuid.uuid4())
        request.state.request_id = rid
        try:
            resp = await call_next(request)
            resp.headers["X-Request-ID"] = rid
            return resp
        except Exception as e:
            raise


def health_status():
    return {"status": "ok"}
