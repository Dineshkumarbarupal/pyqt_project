import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow ,QApplication,QWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from qfluentwidgets import PushButton,FluentIcon

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.resize(900,600)


        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
      
        button = PushButton('Standard push button')

     
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(central_widget)


if __name__=='__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())