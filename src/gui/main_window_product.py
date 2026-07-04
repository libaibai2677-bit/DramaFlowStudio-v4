# DramaFlow Studio v4 - Product Integration UI (Phase 5 Final)
# UI now fully uses SearchFacade as single source of truth

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import QThread, Signal

from src.core.search_facade import SearchFacade


class SearchWorker(QThread):
    result_ready = Signal(list)
    error = Signal(str)

    def __init__(self, facade: SearchFacade, query: str, limit: int = 10):
        super().__init__()
        self.facade = facade
        self.query = query
        self.limit = limit

    def run(self):
        try:
            results = self.facade.search(self.query, self.limit)
            self.result_ready.emit(results)
        except Exception as e:
            self.error.emit(str(e))


class MainWindowProduct(QMainWindow):
    """Final Product UI layer using SearchFacade only"""

    def __init__(self, config=None):
        super().__init__()

        self.config = config or {}
        self.facade = SearchFacade(self.config)
        self.worker = None

        self.setWindowTitle("DramaFlow Studio v4 - AI Product Edition")
        self.setMinimumSize(1100, 750)

        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        self.title = QLabel("AI Visual Search Product (Facade Powered)")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Search images with AI understanding...")

        self.button = QPushButton("Search")
        self.button.clicked.connect(self.on_search)

        self.result_label = QLabel("")

        layout.addWidget(self.title)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_search(self):
        query = self.input.text().strip()
        if not query:
            return

        self.button.setEnabled(False)
        self.result_label.setText("Searching...")

        self.worker = SearchWorker(self.facade, query, limit=10)
        self.worker.result_ready.connect(self.on_results)
        self.worker.error.connect(self.on_error)
        self.worker.finished.connect(lambda: self.button.setEnabled(True))

        self.worker.start()

    def on_results(self, results):
        text = f"Found {len(results)} results\n"

        if results:
            first = results[0]
            text += f"Top intent: {first.get('ai_intent', 'unknown')}\n"
            text += f"AI query: {first.get('ai_query', '')}\n"

        self.result_label.setText(text)

    def on_error(self, err: str):
        self.result_label.setText(f"Error: {err}")
