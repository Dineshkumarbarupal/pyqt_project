import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # self.setWindowTitle("PyQt Window without Menu Button")
        self.resize(900, 700)

        # Center the window on the screen
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        label = BodyLabel("Label")
        label.setTextColor(QColor(0, 255, 0), QColor(255, 0, 0))  # Light theme, dark theme


        # Add a central widget (optional)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        # Add any other widgets to your layout if needed

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the window
    w = Window()
    w.show()

    # Execute the application
    app.exec_()
