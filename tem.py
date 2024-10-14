import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from qfluentwidgets import PrimaryPushButton

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800,500)


        self.central_widget = QWidget()
        layout = QVBoxLayout(self.central_widget)

        button = PrimaryPushButton("Get started ")
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.central_widget)

        

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())
