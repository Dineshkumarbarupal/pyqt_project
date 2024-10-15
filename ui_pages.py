from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSizePolicy, QSpacerItem, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from qfluentwidgets import PrimaryPushButton, BodyLabel, DropDownPushButton, RoundMenu, Action

class FirstPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.init_ui(parent)

    def init_ui(self, parent):
        layout1 = QVBoxLayout(self)
        layout1.addStretch(2)

        image_label = QLabel(self)
        pixmap = QPixmap("whatsapp.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout1.addWidget(image_label)

        layout1.addStretch(1)

        label1 = BodyLabel("Welcome to WhatsApp")
        label1.setFont(QFont("Arial", 15, QFont.Bold))
        label1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label1)

        layout1.addStretch(1)

        label2 = BodyLabel("A simple, reliable, and private way to use WhatsApp on your computer")
        label2.setFont(QFont("Arial", 9))
        label2.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label2)

        layout1.addStretch(1)

        button = PrimaryPushButton('Get started')
        button.clicked.connect(parent.show_second_page)
        layout1.addWidget(button, alignment=Qt.AlignCenter)

        layout1.addStretch(1)

        label3 = BodyLabel("Version 2.2238.6.0")
        label3.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label3)

        layout1.addStretch(3)

class SecondPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.init_ui(parent)

    def init_ui(self, parent):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)
        # layout.addStretch(2)

        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white; border-radius: 10px;")
        central_layout = QVBoxLayout(central_frame)
        central_layout.setAlignment(Qt.AlignCenter)

        central_frame.setMinimumSize(900, 500)
        central_frame.setMaximumWidth(500)
        central_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout.addStretch(1)
        layout.addWidget(central_frame)
        layout.addStretch(1)

        instructions = BodyLabel(
            "<b style='font-size: 16px;'>To set up WhatsApp on your computer</b><br><br>"
            "<span style='color: gray;'>1. Open WhatsApp on your phone</span><br><br>"
            "<span style='color: gray;'>2. Tap <b>Menu</b> on Android, or <b>Settings</b> on iPhone</span><br><br>"
            "<span style='color: gray;'>3. Tap <b>Linked devices</b> and then <b>Link a device</b></span><br><br>"
            "<span style='color: gray;'>4. Point your phone at this screen to capture the QR code</span>"
        )

        instructions.setAlignment(Qt.AlignLeft)
        instructions.setWordWrap(True)
        instructions.setFont(QFont("Arial", 10))
        instructions.setStyleSheet("padding-left: 30px; line-height: 35px;")

        central_layout.addWidget(instructions)

        spacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        central_layout.addSpacerItem(spacer)

        link_label = BodyLabel('<a href="#">Link with phone number</a>')
        link_label.setAlignment(Qt.AlignLeft)
        link_label.setFont(QFont("Arial", 9, QFont.Bold))
        link_label.setOpenExternalLinks(False)
        link_label.linkActivated.connect(parent.show_third_page)  
        link_label.setStyleSheet("padding-left: 33px;")  
        central_layout.addWidget(link_label)

        qr_label = QLabel(self)
        pixmap = QPixmap("qr2.png")  
        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignRight) 

        central_layout.addWidget(qr_label)

        central_layout.addStretch(1)

        self.setLayout(layout)

class ThirdPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white; border-radius: 10px;")
        central_frame.setFixedSize(900, 600)

        central_layout = QVBoxLayout(central_frame)

        label = BodyLabel("Enter phone number", central_frame)
        label.setFont(QFont("Arial", 11))
        label.setAlignment(Qt.AlignCenter)
        central_layout.addWidget(label)

        central_layout.addStretch(1)

        label2 = BodyLabel("Select a country and your WhatsApp phone number", central_frame)
        label2.setFont(QFont("Arial", 11))
        label2.setAlignment(Qt.AlignCenter)
        central_layout.addWidget(label2)

        central_layout.addStretch(1)

        button = DropDownPushButton('Select country/region')
        menu = RoundMenu(parent=button)

        search_box = QLineEdit(menu)
        search_box.setPlaceholderText("Search country/region")
        menu.setFixedSize(200, 100)
        menu.layout().addWidget(search_box)

        button.setMenu(menu)
        button.setFixedSize(195, 40)
        central_layout.addWidget(button)

        central_layout.addStretch(1)

        self.setLayout(layout)

