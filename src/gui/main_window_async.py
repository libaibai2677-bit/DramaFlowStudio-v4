# DramaFlow Studio v4 - Async Main Window (Non-blocking MVP UI)

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem
)

from src.app.application import Application
from src.app.workers import SearchWorker


class MainWindowAsync(QMainWindow):
    """
    Async version of MainWindow.
    Uses SearchWorker to avoid UI blocking.
    """

    def __init__(self, config=None):
        super().__init__()
        self.config = config or {}

        self.app_core = Application(self.config)
        self.worker = None

        self.setWindowTitle("DramaFlow Studio v4 - Async MVP")
        self.setMinimumSize(1000, 700)

        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        self.title = QLabel("DramaFlow Studio v4 - Async Image Search")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter prompt...")

        self.button = QPushButton("Search")
        self.button.clicked.connect(self.on_search)

        self.results = QListWidget()

        layout.addWidget(self.title)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.results)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_search(self):
        query = self.input.text().strip()
        if not query:
            return

        self.results.clear()
        self.button.setEnabled(False)

        self.worker = SearchWorker(self.app_core, query, limit=10)
        self.worker.result_ready.connect(self.on_results)
        self.worker.error.connect(self.on_error)
        self.worker.finished.connect(lambda: self.button.setEnabled(True))

        self.worker.start()

    def on_results(self, data):
        for item in data:
            text = f"[{item.get('source','')}] {item.get('title','')}"
            self.results.addItem(QListWidgetItem(text))

    def on_error(self, err: str):
        self.results.addItem(QListWidgetItem(f"Error: {err}"))
