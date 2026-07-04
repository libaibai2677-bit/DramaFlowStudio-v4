# 🧱 Production Hardening Layer (Bootstrap)
# System-wide initialization: config, logging, DI, runtime wiring

import os
import logging
from dataclasses import dataclass
from typing import Any

from src.domain.orchestrator.agent_orchestrator import AgentOrchestrator
from src.domain.tools.web_search_tool import WebSearchTool
from src.domain.tools.real_web_search_tool import RealWebSearchTool
from src.domain.services.tool_registry import ToolRegistry


# -----------------------------
# ⚙️ Config Layer
# -----------------------------
@dataclass
class Settings:
    env: str = os.getenv("ENV", "dev")
    web_provider: str = os.getenv("WEB_SEARCH_PROVIDER", "serpapi")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()


# -----------------------------
# 📜 Logging Setup
# -----------------------------

def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
    )

    logger = logging.getLogger("DramaFlowRuntime")
    logger.info("Logging initialized")
    return logger


logger = setup_logging()


# -----------------------------
# 🧩 Dependency Injection Container (Lightweight)
# -----------------------------
class Container:
    """
    Simple DI container for runtime components.
    """

    def __init__(self):
        self.tools = ToolRegistry()

        # 🌐 Web search (switchable provider)
        if settings.env == "prod":
            self.web = RealWebSearchTool()
        else:
            self.web = WebSearchTool()

        self.orchestrator = AgentOrchestrator(tools=self.tools)

    def get_orchestrator(self) -> AgentOrchestrator:
        return self.orchestrator

    def get_tools(self) -> ToolRegistry:
        return self.tools

    def get_web(self) -> Any:
        return self.web


# -----------------------------
# 🚀 Global Runtime Bootstrap
# -----------------------------
container = Container()
orchestrator = container.get_orchestrator()

logger.info("AI Runtime Bootstrap completed")


# -----------------------------
# 🧠 Runtime Health Check Helper
# -----------------------------
def runtime_status():
    return {
        "status": "running",
        "env": settings.env,
        "web_provider": settings.web_provider,
        "log_level": settings.log_level,
    }