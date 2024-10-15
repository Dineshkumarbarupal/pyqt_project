from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout,QLabel, QFrame
from PyQt5.QtGui import QFont, QPixmap
from qfluentwidgets import BodyLabel,PrimaryPushButton

class First_page(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.init_ui(parent)

    def init_ui(self,parant):

        layout1 = QVBoxLayout(self)
        layout1.addStretch(2)

        image_label = QLabel(self)
        pixmap = QPixmap("whatsapp.png")
        image_label.setPixmap(pixmap)
        layout1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(image_label)

        layout1.addStretch(1)

        label1 = QLabel("Welcome to WhatsApp")
        label1.setFont(QFont("Arial",15, QFont.Bold))
        label1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label1)

        layout1.addStretch(1)

        label2 = QLabel("A simpal,reliable and private way to use WhatsApp on your computer")
        label2.setFont(QFont("Arial",9))
        label2.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label2)

        layout1.addStretch(1)

        button = PrimaryPushButton("Get started")
        # button.clicked.connect(parant.show_second_page)
        layout1.addWidget(button,alignment=Qt.AlignCenter)

        layout1.addStretch(1)

        label3 = QLabel("Version 2.2238.6.0")
        label3.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label3)
        
        layout1.addStretch(3)

class Second_page(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.init_ui(parent)
        

    # def init_ui(self,parent):
    #     layout = QVBoxLayout(self)
    #     layout.setContentsMargins(15,15,15,15)
    #     # layout.setAlignment(Qt.AlignCenter)
    #     layout.addStretch(1)

    #     central_frame = QFrame(self)
    #     central_frame.setStyleSheet("background-color: white; border-radius:10px")
    #     central_layout = QVBoxLayout(central_frame)
    #     central_layout.setAlignment(Qt.AlignCenter)





