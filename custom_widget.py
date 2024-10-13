from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor

class TitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def setTextColor(self, light_color: QColor, dark_color: QColor):
        self.setStyleSheet(f"color:rgb({light_color.red()},{light_color.green()},{light_color.blue()});")
