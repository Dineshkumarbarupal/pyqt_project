import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from qfluentwidgets import BodyLabel

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label = BodyLabel("this is my practice")
       
        layout.addWidget(label)

        self.setCentralWidget(central_widget)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())