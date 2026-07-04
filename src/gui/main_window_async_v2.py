# DramaFlow Studio v4 - FINAL Async Grid MVP (v2 Safe Version)
# This version avoids overwrite conflicts and is production-safe structure

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from src.app.application import Application
from src.app.workers import SearchWorker
from src.gui.image_grid_widget import ImageGridWidget


class MainWindowAsyncV2(QMainWindow):
    """
    Final MVP version of DramaFlow Studio v4 UI.

    Features:
    - Async non-blocking search
    - Image grid thumbnail display
    - Clean application-layer architecture
    - Safe standalone UI version (v2)
    """

    def __init__(self, config=None):
        super().__init__()

        self.config = config or {}
        self.app_core = Application(self.config)
        self.worker = None

        self.setWindowTitle("DramaFlow Studio v4 - FINAL GRID MVP")
        self.setMinimumSize(1100, 750)

        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        # Header
        self.title = QLabel("AI Image Search Studio - Grid MVP")

        # Input
        self.input = QLineEdit()
        self.input.setPlaceholderText("Type anything to search images...")

        # Button
        self.button = QPushButton("Search")
        self.button.clicked.connect(self.on_search)

        # Grid
        self.grid = ImageGridWidget()

        # Layout
        layout.addWidget(self.title)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.grid)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def on_search(self):
        query = self.input.text().strip()
        if not query:
            return

        # Reset UI state
        self.grid.clear_images()
        self.button.setEnabled(False)

        # Start async worker
        self.worker = SearchWorker(self.app_core, query, limit=12)
        self.worker.result_ready.connect(self.on_results)
        self.worker.error.connect(self.on_error)
        self.worker.finished.connect(lambda: self.button.setEnabled(True))

        self.worker.start()

    def on_results(self, data):
        for item in data:
            title = item.get("title", "")
            thumb = item.get("thumbnail", "")

            self.grid.add_image(title, thumb)

    def on_error(self, err: str):
        self.grid.add_image(f"Error: {err}", "")
