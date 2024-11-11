import sys
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtGui import QIcon
from ui_pages import FirstPage, SecondPage, ThirdPage
from qfluentwidgets import SplashScreen
from qframelesswindow import FramelessWindow

class SplashScreenWindow(FramelessWindow):
    def __init__(self, icon_path, main_window, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 400)  # Set splash screen size
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowTitle('')  # Empty title for splash screen
        self.setWindowIcon(QIcon(icon_path))
        self.main_window = main_window  # Reference to main window
        self.splashscreen = SplashScreen(self.windowIcon(), self)
        self.splashscreen.setIconSize(QSize(200, 200))  # Adjust icon size as needed
        self.splashscreen.show()

    def closeEvent(self, event):
        # Show main window when splash screen is closed
        self.main_window.show()
        super().closeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.init_window()

    def init_window(self):
        self.resize(900, 700)
        
        screen = QApplication.primaryScreen().availableGeometry()
        w, h = screen.width(), screen.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        self.first_page = FirstPage(self)
        self.central_widget.addWidget(self.first_page)

        self.second_page = SecondPage(self)
        self.central_widget.addWidget(self.second_page)

        self.third_page = ThirdPage(self)
        self.central_widget.addWidget(self.third_page)

    def show_second_page(self):
        self.central_widget.setCurrentWidget(self.second_page)

    def show_third_page(self):
        self.central_widget.setCurrentWidget(self.third_page)

if __name__ == '__main__':
    # Set DPI attributes
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    # Create the main window but keep it hidden initially
    window = MainWindow()
    window.hide()

    icon_path = 'C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp3-removebg-preview.png'
    splash_screen = SplashScreenWindow(icon_path, window)
    splash_screen.show()

    # Close splash screen and show main window after delay
    QTimer.singleShot(3000, splash_screen.close)

    sys.exit(app.exec_())
