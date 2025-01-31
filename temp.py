from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QStyle,QVBoxLayout,QToolButton,QLabel, QFrame,QSizePolicy,QSpacerItem,QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from qfluentwidgets import BodyLabel,PrimaryPushButton,PushButton,DropDownPushButton,FluentIcon,Action,RoundMenu

class First_page(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.pixmap = QPixmap("whatsapp3_logo-removebg-preview.png")
        self.init_ui(parent)

    def init_ui(self,parant):

        layout1 = QVBoxLayout(self)
        layout1.addStretch(1)

        self.image_label = QLabel(self)
        self.update_image_size(200,200)    
        layout1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.image_label)

        layout1.addStretch(0)

        label1 = QLabel("Welcome to WhatsApp")
        label1.setFont(QFont("Arial",15, QFont.Bold))
        label1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label1)

        layout1.addSpacing(17)

        label2 = QLabel("A simpal,reliable and private way to use WhatsApp on your computer")
        label2.setFont(QFont("Arial",10))
        label2.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label2)

        layout1.addSpacing(20)

        button = PrimaryPushButton("Get started")
        button.setFixedSize(180,30)
        button.clicked.connect(parant.show_second_page)
        layout1.addWidget(button,alignment=Qt.AlignCenter)

        layout1.addSpacing(20)

        label3 = QLabel("Version 2.2440.9.0")
        label3.setFont(QFont("Arial",10))
        label3.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label3)

        layout1.addStretch(1)

    def update_image_size(self,width,height):
        scaled_Pixmap = self.pixmap.scaled(width,height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_Pixmap)
    
    def resizeEvent(self,event):
        new_width = self.width() * 0.5
        new_height = self.height() * 0.5
        self.update_image_size(int(new_width),int(new_height))
        super().resizeEvent(event)

class Second_page(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.init_ui(parent)

    def init_ui(self, parent):  
        layout = QVBoxLayout()
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setAlignment(Qt.AlignCenter)
     
        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white; border-radius: 10px")
        central_frame.setMinimumSize(900, 600)
        central_frame.setMaximumWidth(500)
        
        central_layout = QVBoxLayout(central_frame)

        instruction = BodyLabel(
            "<b style='font-size:18px;'>To set up WhatsApp on your computer</b><br><br>"
            "<span style='color: gray;'>1. Open WhatsApp on your phone</span><br><br>"
            "<span style='color: gray;'>2. Tap <b>Menu</b> on Android, or <b>Settings</b> on iPhone</span><br><br>"
            "<span style='color: gray;'>3. Tap <b>Linked devices</b> and then <b>Link a device</b></span><br><br>"
            "<span style='color: gray;'>4. point your phone at this screen to capture the QR code</span><br><br>"
        )

        instruction.setAlignment(Qt.AlignLeft)
        instruction.setFont(QFont("Arial", 11))
        instruction.setStyleSheet("padding-left: 100px; line-height: 100px;padding-top:100px;")
        instruction.setWordWrap(True)

        qr_label = QLabel(self)
        pixmap = QPixmap("qr2.png")  
        qr_label.setPixmap(pixmap)
        qr_label.setStyleSheet("padding-top:100px; padding-right:100px;")
        qr_label.setAlignment(Qt.AlignRight)

        line_layout = QHBoxLayout()
        line_layout.addWidget(instruction)
        line_layout.addWidget(qr_label)

        central_layout.addLayout(line_layout)

        link_label = BodyLabel("<a href='#' style='color: green;'>Link with phone number</a>")
        link_label.setAlignment(Qt.AlignLeft)
        link_label.linkActivated.connect(parent.show_third_page)
        link_label.setFont(QFont("Arial", 9, QFont.Bold))
        link_label.setStyleSheet("padding-left: 100px;padding-bottom: 100px")  

        central_layout.addWidget(link_label)

        layout.addWidget(central_frame)

        back_button = QToolButton(self)
        back_button.setIcon(self.style().standardIcon(QStyle.SP_ArrowBack))
        back_button.clicked.connect(parent.show_first_page)

        layout.addWidget(back_button, alignment=Qt.AlignLeft | Qt.AlignTop)

        self.setLayout(layout)


class Third_page(QWidget):
    def __init__(self,parant):
        super().__init__()
        self.init_ui(parant)

    def init_ui(self,parant):

        layout2 = QVBoxLayout()
        layout2.setContentsMargins(1,10,10,10)
        layout2.setAlignment(Qt.AlignCenter)

        central_frame = QFrame(self)
        central_frame.setStyleSheet("background-color: white")
        central_frame.setFixedSize(888,500)
        # central_frame.setM(500)

        central_layout = QVBoxLayout(central_frame)
        
        label = BodyLabel("<b>Enter phone number</b>")
        label.setFont(QFont("Arial",14))
        label.setAlignment(Qt.AlignCenter)
        central_layout.addWidget(label)

        label2 = BodyLabel("Select a country and add your phone number")
        label2.setStyleSheet("padding-bottom: 100px;")
        label2.setAlignment(Qt.AlignCenter)
        central_layout.addWidget(label2)
        central_layout.setContentsMargins(0,0,0,290)

        button2 = DropDownPushButton(FluentIcon.MAIL, 'Email')
        # Create menu
        menu = RoundMenu(parent=button2)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("What are you doing?")))
        menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("I like singing, rapping, and dancing")))
        menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("Just because you are so beautiful")))
        # Add menu
        button2.setMenu(menu)

        central_layout.setAlignment(Qt.AlignCenter)

        central_layout.addWidget(button2)


        layout2.addWidget(central_frame, alignment= Qt.AlignCenter)

        self.setLayout(layout2)
    
        

