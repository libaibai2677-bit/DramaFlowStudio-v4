# DramaFlow Studio v4 - Main Window

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self, config=None):
        super().__init__()
        self.config = config or {}

        self.setWindowTitle("DramaFlow Studio v4")
        self.setMinimumSize(1000, 700)

        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        title = QLabel("DramaFlow Studio v4")
        subtitle = QLabel("Image Search Engine - Stage 1")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()

        central.setLayout(layout)
        self.setCentralWidget(central)
