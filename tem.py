import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QStackedWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from temp import First_page,Second_page


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        self.resize(900,600)

        
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        self.first_page = First_page(self)
        self.central_widget.addWidget(self.first_page)

        self.second_page = Second_page(self)
        self.central_widget.addWidget(self.second_page)
  
    def show_second_page(self):
        self.central_widget.setCurrentWidget(self.second_page)
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())




