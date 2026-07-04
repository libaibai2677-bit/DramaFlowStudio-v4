# DramaFlow Studio v4 - Logger System

import logging
import os
from datetime import datetime


def get_logger(name: str = "DramaFlow"):
    """Create and return a configured logger."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    log_file = f"logs/dramaflow_{datetime.now().strftime('%Y%m%d')}.log"

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
