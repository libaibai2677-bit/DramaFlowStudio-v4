# DramaFlow Studio v4 - Image Grid Widget (Thumbnail View)

from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize
import requests
from io import BytesIO


class ImageGridWidget(QListWidget):
    """
    Simple thumbnail grid widget for displaying image search results.
    MVP version (no caching yet).
    """

    def __init__(self):
        super().__init__()
        self.setViewMode(QListWidget.IconMode)
        self.setIconSize(QSize(160, 160))
        self.setResizeMode(QListWidget.Adjust)
        self.setGridSize(QSize(180, 180))

    def clear_images(self):
        self.clear()

    def add_image(self, title: str, thumbnail_url: str):
        try:
            response = requests.get(thumbnail_url, timeout=10)
            image_data = BytesIO(response.content)

            pixmap = QPixmap()
            pixmap.loadFromData(image_data.read())

            icon = QIcon(pixmap)

            item = QListWidgetItem(icon, title)
            self.addItem(item)

        except Exception:
            self.addItem(QListWidgetItem(title))
