import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QDesktopWidget, QSplashScreen
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from temp import First_page, Second_page, Third_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.splash_screen_width = 200
        self.splash_screen_height = 200
        self.setFixedSize(960, 720)  # main window dimensions
        self.setWindowTitle('WhatsApp')
        self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp3-removebg-preview.png'))

        pixmap = QPixmap('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp3-removebg-preview.png').scaled(
            self.splash_screen_width, self.splash_screen_height, Qt.KeepAspectRatio
        )

        self.splashScreen = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.splash_screen_width) // 2
        y = (screen_geometry.height() -self.splash_screen_height) // 2
        self.splashScreen.move(x, y)

        self.splashScreen.show()
        QTimer.singleShot(3000, self.show_main_window)

        self.center_main_window()
        # self.initwindow()
        self.window()

    def show_main_window(self):
        self.splashScreen.finish(self)
        self.show()

    def center_main_window(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen_geometry.center())
        self.move(frame_geometry.topLeft())

    def initwindow(self):
            self.resize(900,400)
            self.setWindowTitle('WhatsApp')
            self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp_logo.png'))
             
            desktop = QApplication.desktop().availableGeometry()
            w,h  = desktop.width(),desktop.height()
            self.move(w//2 - self.width(), h//2 - self.height())

    def window(self):

        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        self.first_page = First_page(self)
        self.central_widget.addWidget(self.first_page)

        self.second_page = Second_page(self)
        self.central_widget.addWidget(self.second_page)

        self.third_page = Third_page(self)
        self.central_widget.addWidget(self.third_page)

    def show_first_page(self):
        self.central_widget.setCurrentWidget(self.first_page)

    def show_second_page(self):
        self.central_widget.setCurrentWidget(self.second_page)

    def show_third_page(self):
        self.central_widget.setCurrentWidget(self.third_page)

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
