import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Outer layout
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(20, 20, 20, 20)
        outer_layout.addStretch(1)  # Add spacing to center the box vertically

        # Create a central frame (like the inner box in your image)
        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white; border-radius: 10px;")
        central_layout = QVBoxLayout(central_frame)

        central_frame.setMinimumSize(1000, 600)  # Reduced size for responsiveness
        central_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        central_layout.addStretch(0)
        # Add text instructions
        instructions = QLabel(self)
        instructions.setText(
            "<b>To set up WhatsApp on your computer</b><br><br>"
            "1. Open WhatsApp on your phone<br>"
            "2. Tap <b>Menu</b> on Android, or <b>Settings</b> on iPhone<br>"
            "3. Tap <b>Linked devices</b> and then <b>Link a device</b><br>"
            "4. Point your phone at this screen to capture the QR code"
        )
        instructions.setAlignment(Qt.AlignLeft)
        instructions.setWordWrap(True)
        instructions.setFont(QFont("Arial", 12))
        instructions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_layout.addWidget(instructions)

        # Add QR Code image
        qr_label = QLabel(self)
        pixmap = QPixmap("path/to/qr_code_image.png")
        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignCenter)
        qr_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_layout.addWidget(qr_label)

        # Add link with phone number
        link_label = QLabel(self)
        link_label.setText('<a href="#">Link with phone number</a>')
        link_label.setAlignment(Qt.AlignLeft)
        link_label.setFont(QFont("Arial", 10, QFont.Bold))
        link_label.setOpenExternalLinks(True)
        central_layout.addWidget(link_label)

        # Add the central frame (inner box) to the outer layout
        outer_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        outer_layout.addStretch(1)  # Add more spacing to center the box vertically

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Setup")
        self.setGeometry(200, 100, 800, 600)

        # Load second page
        second_page = SecondPage()
        self.setCentralWidget(second_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
