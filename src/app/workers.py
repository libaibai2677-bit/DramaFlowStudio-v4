# DramaFlow Studio v4 - Async Workers
# Provides non-blocking execution for image search

from PySide6.QtCore import QThread, Signal
from typing import Dict, Any, List


class SearchWorker(QThread):
    """
    Async worker for image search to prevent UI blocking.
    """

    result_ready = Signal(list)
    error = Signal(str)

    def __init__(self, application, query: str, limit: int = 10):
        super().__init__()
        self.application = application
        self.query = query
        self.limit = limit

    def run(self):
        try:
            results = self.application.search_images(self.query, self.limit)
            self.result_ready.emit(results)
        except Exception as e:
            self.error.emit(str(e))
