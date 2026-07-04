# 📊 DramaFlow AI - Observability Full Stack (Metrics + Tracing + Logging)

import time
import uuid
import json
import logging
from prometheus_client import Counter, Histogram
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

# -----------------------------
# Logging Layer (Structured)
# -----------------------------

logger = logging.getLogger("dramaflow-observability")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)


def log_event(event: str, **kwargs):
    logger.info(json.dumps({
        "event": event,
        "ts": time.time(),
        **kwargs
    }))


# -----------------------------
# Metrics Layer (Prometheus)
# -----------------------------

REQUEST_COUNT = Counter(
    "dramaflow_requests_total",
    "Total number of requests",
    ["method", "path", "status"]
)

REQUEST_LATENCY = Histogram(
    "dramaflow_request_latency_seconds",
    "Request latency in seconds",
    ["method", "path"]
)


# -----------------------------
# Tracing Layer (Lightweight)
# -----------------------------

def generate_trace_id():
    return str(uuid.uuid4())


# -----------------------------
# Observability Middleware
# -----------------------------

class ObservabilityStackMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = generate_trace_id()
        start_time = time.time()

        request.state.trace_id = trace_id

        log_event(
            "request_start",
            trace_id=trace_id,
            path=request.url.path,
            method=request.method
        )

        try:
            response = await call_next(request)
            duration = time.time() - start_time

            REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
            REQUEST_LATENCY.labels(request.method, request.url.path).observe(duration)

            log_event(
                "request_end",
                trace_id=trace_id,
                status=response.status_code,
                duration=duration
            )

            response.headers["X-Trace-ID"] = trace_id
            return response

        except Exception as e:
            log_event(
                "request_error",
                trace_id=trace_id,
                error=str(e)
            )
            raise


# -----------------------------
# Health + Metrics Helpers
# -----------------------------

def health_check():
    return {
        "status": "ok",
        "service": "dramaflow-ai",
        "timestamp": time.time()
    }


def metrics_snapshot():
    return {
        "status": "metrics_available",
        "note": "Expose /metrics endpoint via prometheus_client in FastAPI"
    }
