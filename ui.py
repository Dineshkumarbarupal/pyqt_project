import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QColor, QFont, QPixmap  # Import QPixmap for the image

class TitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def setTextColor(self, light_color, dark_color):
        self.setStyleSheet(f"color:rgb({light_color.red()},{light_color.green()},{light_color.blue()});")

class PrimaryPushButton(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;")
        self.setFont(QFont("Alice", 12))
        self.setFixedSize(200,33)

class Window(QMainWindow):

    def __init__(self): 
        super().__init__()
        self.initwindow()

    def initwindow(self):
        self.resize(900, 700)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        layout.addStretch(1)

        # Add an image (PNG file)
        image_label = QLabel(self)
        pixmap = QPixmap("https://gurpreetsingh.aliens.school/whatsapp.png")  # Replace with your image path
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)  # Center the image
        layout.addWidget(image_label)

        # Create "Welcome to WhatsApp" text label
        label1 = TitleLabel("Welcome to WhatsApp")
        font1 = QFont()
        font1.setPointSize(20)  # Set font size for the welcome text
        label1.setFont(font1)
        label1.setStyleSheet("font-weight: bold;")  # Make text bold
        label1.setAlignment(Qt.AlignCenter)  # Align the label to the center
        label1.setTextColor(QColor(0, 0, 0), QColor(255, 255, 255))  # Light theme, dark theme
        layout.addWidget(label1)

        label2 = TitleLabel("A simple, reliable, and private way to use WhatsApp on your computer")
        font2 = QFont()
        font2.setPointSize(10)
        label2.setFont(font2)
        label2.setStyleSheet("font-weight: light;")
        label2.setAlignment(Qt.AlignCenter)
        label2.setTextColor(QColor(0, 0, 0), QColor(255, 255, 255))
        layout.addWidget(label2)

        # Add button
        button = PrimaryPushButton('Get started')
        layout.addWidget(button, alignment=Qt.AlignCenter)

        # Version label
        label3 = TitleLabel("Version 2.2238.6.0")
        font3 = QFont()
        font3.setPointSize(9)
        label3.setFont(font3)
        label3.setAlignment(Qt.AlignCenter)
        layout.addWidget(label3)

        layout.addStretch(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
