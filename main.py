import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui_pages import FirstPage, SecondPage, ThirdPage

class Window(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.init_window()

    def init_window(self):
        self.resize(900, 700)
        
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
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
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
