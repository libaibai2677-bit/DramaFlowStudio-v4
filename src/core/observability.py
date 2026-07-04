# 📊 Observability Layer (Production Final Optimization)
# Trace logging + execution visibility for AI runtime

import time
import uuid
import logging
from contextvars import ContextVar
from typing import Dict, Any, Optional


# -----------------------------
# 🧠 Trace Context
# -----------------------------
trace_id_ctx: ContextVar[str] = ContextVar("trace_id", default=None)


def get_trace_id() -> str:
    trace_id = trace_id_ctx.get()
    if not trace_id:
        trace_id = str(uuid.uuid4())
        trace_id_ctx.set(trace_id)
    return trace_id


def set_trace_id(trace_id: Optional[str] = None):
    trace_id = trace_id or str(uuid.uuid4())
    trace_id_ctx.set(trace_id)
    return trace_id


# -----------------------------
# 📜 Logger
# -----------------------------
logger = logging.getLogger("DramaFlowObservability")


# -----------------------------
# ⏱️ Execution Span
# -----------------------------
class Span:
    """
    Represents a single execution unit in the AI system.
    """

    def __init__(self, name: str, metadata: Optional[Dict[str, Any]] = None):
        self.name = name
        self.metadata = metadata or {}
        self.start_time = None
        self.end_time = None
        self.trace_id = get_trace_id()

    def __enter__(self):
        self.start_time = time.time()
        logger.info(f"[TRACE:{self.trace_id}] START span={self.name} meta={self.metadata}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        duration = self.end_time - self.start_time

        status = "error" if exc_type else "ok"

        logger.info(
            f"[TRACE:{self.trace_id}] END span={self.name} status={status} duration={duration:.4f}s"
        )


# -----------------------------
# 🧭 Observability Helper
# -----------------------------
class Observability:
    """
    Central tracing utility for AI runtime.
    """

    @staticmethod
    def start_trace(trace_id: Optional[str] = None) -> str:
        return set_trace_id(trace_id)

    @staticmethod
    def get_context() -> Dict[str, Any]:
        return {
            "trace_id": get_trace_id()
        }

    @staticmethod
    def span(name: str, metadata: Optional[Dict[str, Any]] = None):
        return Span(name, metadata)


# -----------------------------
# 🚀 Middleware Hook (for API integration)
# -----------------------------
async def inject_trace_middleware(request_id: Optional[str] = None):
    """
    Used by FastAPI middleware to inject trace context.
    """
    set_trace_id(request_id)
    logger.info(f"Trace initialized: {get_trace_id()}")