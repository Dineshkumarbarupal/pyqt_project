import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,QVBoxLayout
from qfluentwidgets import PrimaryPushButton

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        # self.setStyleSheet("init_ui{background: rgb(225,225,225)}")

    def init_ui(self):
        self.resize(500,300)

        layout = QVBoxLayout(self)

        button = PrimaryPushButton("pussbutton")
     
        
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())
