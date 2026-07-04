# 📊 Infrastructure Layer — Logging (Scale Phase)

import logging
import uuid

class Logger:
    """
    Centralized logging system for observability.
    Adds request tracing capability.
    """

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger("DramaFlowStudio")

    def log(self, message: str, level: str = "info", request_id: str = None):
        if request_id is None:
            request_id = str(uuid.uuid4())

        formatted = f"[request_id={request_id}] {message}"

        if level == "info":
            self.logger.info(formatted)
        elif level == "error":
            self.logger.error(formatted)
        elif level == "warning":
            self.logger.warning(formatted)
        else:
            self.logger.info(formatted)

        return request_id
