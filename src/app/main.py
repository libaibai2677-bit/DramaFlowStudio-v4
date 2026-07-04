# DramaFlow Studio v4 - Application Entry

import sys
from PySide6.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.core.logger import get_logger
from src.core.config import load_config

logger = get_logger(__name__)


def main():
    logger.info("Starting DramaFlow Studio v4...")

    # Load config
    config = load_config()

    app = QApplication(sys.argv)

    window = MainWindow(config=config)
    window.show()

    logger.info("UI launched successfully.")

    sys.exit(app.exec())
