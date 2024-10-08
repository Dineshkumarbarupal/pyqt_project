import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from qfluentwidgets import PushButton,FluentIcon,PrimaryToolButton

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.resize(900,400)  
    
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        button = PushButton('Standard push button')
            
        button.setFixedSize(200,60)
        
        layout.addWidget(button)
        layout.addWidget(button,alignment= Qt.AlignCenter)


        button2 = PushButton(FluentIcon.FOLDER, 'Standard push button with icon')
        button2 = PushButton(QIcon("/path/to/icon.png"), 'Standard push button with icon')
        button2.setFixedSize(300,60)
        layout.addWidget(button2)
        layout.addWidget(button2,alignment= Qt.AlignCenter)
        layout.addStretch(0)

        button3 = PrimaryToolButton(FluentIcon.FOLDER)
        button3 = PrimaryToolButton(QIcon("/path/to/icon.png"))
        button3.setFixedSize(100,40)
        layout.addWidget(button3)
        layout.addWidget(button3,alignment= Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())