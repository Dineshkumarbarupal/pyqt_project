import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QStackedWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from temp import First_page,Second_page,Third_page

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window()
        self.initwindow()

    def initwindow(self):
            self.resize(900,400)
            self.setWindowTitle('WhatsApp')
            self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp_logo.png'))
            
            desktop = QApplication.desktop().availableGeometry()
            w,h = desktop.width(),desktop.height()
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
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())




