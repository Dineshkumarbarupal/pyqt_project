from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout,QLabel, QFrame,QSizePolicy,QSpacerItem
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
        button.clicked.connect(parant.show_second_page)
        layout1.addWidget(button,alignment=Qt.AlignCenter)

        layout1.addStretch(1)

        label3 = QLabel("Version 2.2238.6.0")
        label3.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label3)
        
        layout1.addStretch(3)

class Second_page(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.init_ui(parent)
        

    def init_ui(self,parent):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15,15,15,15)
        layout.setAlignment(Qt.AlignCenter)
        layout.addStretch(1)

        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white; border-radius:10px")
        central_layout = QVBoxLayout(central_frame)
        central_layout.setAlignment(Qt.AlignCenter)

        central_frame.setMinimumSize(900,500)
        central_frame.setMaximumWidth(500)
        central_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addStretch(1)
        layout.addWidget(central_frame)
        layout.addStretch(1)


        instruction = BodyLabel(
            "<b style='font-size;16px:'>To set up WhatsApp on your computer </b><br><br>"
            "<span style= 'color: gray;'>1. Open WhatsApp on your phone</span><br><br>"
            "<span style= 'color: gray;'>2. Tab <b>Manu</b> on Android, or <b>Settings</b> on iphone</span><br><br>"
            "<span style= 'color: gray;'>3. Tap <b>Linked devices</b> and than <b>link a divice</b></span><br><br>"
            "<span style= 'color: gray;'>4. Point your phone at this screen to capture the QR code"
        )
        instruction.setAlignment(Qt.AlignLeft)
        instruction.setFont(QFont("Arial", 10))
        instruction.setStyleSheet("padding-left: 30px; line-height: 35px;")

        central_layout.addWidget(instruction)

        spacer = QSpacerItem(100,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        central_layout.addSpacerItem(spacer)

        link_label = BodyLabel("<a href= '#'> Link with phone number </a>")
        link_label.setAlignment(Qt.AlignLeft)
        link_label.setFont(QFont("Arial",9, QFont.Bold))
        central_layout.addWidget(link_label)


        qr_label = QLabel(self)
        pixmap = QPixmap("qr2.png")
        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignRight)
        




        











