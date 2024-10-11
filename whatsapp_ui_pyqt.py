import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget, QWidget, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QFont, QPixmap
from qfluentwidgets import PushButton, PrimaryPushButton, FluentIcon, TitleLabel, BodyLabel, DropDownPushButton, RoundMenu,Action, SplitPushButton

class TitleLabel(QLabel):
    
    def __init__(self, text):
        super().__init__(text)

    def setTextColor(self, light_color, dark_color):
        self.setStyleSheet(f"color:rgb({light_color.red()},{light_color.green()},{light_color.blue()});")

class Window(QMainWindow):

    def __init__(self): 
        super().__init__()
        self.initwindow()

    def initwindow(self):
        self.resize(900, 700)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
       
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)
      
        self.first_page = QWidget()
        layout1 = QVBoxLayout(self.first_page)

        layout1.addStretch(2)

        image_label = QLabel(self.first_page)
        pixmap = QPixmap("whatsapp.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout1.addWidget(image_label)

        layout1.addStretch(1)

        # Use Fluent Title Label for Welcome Text
        label1 = BodyLabel("Welcome to WhatsApp")
        font1 = QFont()
        font1.setPointSize(15)
        label1.setFont(font1)
        label1.setStyleSheet("font-weight: bold;")
        label1.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label1)

        layout1.addStretch(1)

        # Fluent InfoLabel for the description
        label2 = BodyLabel("A simple, reliable, and private way to use WhatsApp on your computer")
        font2 = QFont()
        font2.setPointSize(9)
        label2.setFont(font2)
        label2.setStyleSheet("font-weight: light;")
        label2.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label2)

        layout1.addStretch(1)

        # Fluent PrimaryPushButton for 'Get Started'
        button = PrimaryPushButton('Get started')
        button.clicked.connect(self.show_second_page)
        layout1.addWidget(button, alignment=Qt.AlignCenter)

        layout1.addStretch(1)

        # Use Fluent InfoLabel for Version
        label3 = BodyLabel("Version 2.2238.6.0")
        font3 = QFont()
        font3.setPointSize(10)
        label3.setFont(font3)
        label3.setAlignment(Qt.AlignCenter)
        layout1.addWidget(label3)

        layout1.addStretch(3)

        self.central_widget.addWidget(self.first_page)
    
        # Second Page
        self.second_page = QWidget()
        self.init_ui() 
        self.central_widget.addWidget(self.second_page)

        # Third Page (for Link with phone number)
        self.third_page = QWidget()
        self.init_third_page()  # Initialize third page
        self.central_widget.addWidget(self.third_page)

    def show_second_page(self):
        """Switch to second page when button is clicked"""
        self.central_widget.setCurrentWidget(self.second_page) 

    def init_ui(self):
      
        outer_layout = QVBoxLayout()  # Remove the page assignment here
        outer_layout.setContentsMargins(20, 20, 20, 20)
        outer_layout.addStretch(1)  
      
        central_frame = QFrame(self.second_page)
        central_frame.setStyleSheet("background-color: white; border-radius: 10px;")
        central_layout = QVBoxLayout(central_frame)

        central_frame.setMinimumSize(1000, 600)
        central_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        central_layout.addStretch(1)
      
        h_layout = QVBoxLayout() 

        # Fluent InfoLabel for instructions
        instructions = BodyLabel(
            "<b style= 'font-size: 16px;'>To set up WhatsApp on your computer</b><br><br>"
            "<span style='color: gray;'>1. Open WhatsApp on your phone</span><br><br>"
            "<span style='color: gray;'>2. Tap <b>Menu</b> on Android, or <b>Settings</b> on iPhone</span><br><br>"
            "<span style='color: gray;'>3. Tap <b>Linked devices</b> and then <b>Link a device</b></span><br><br>"
            "<span style='color: gray;'>4. Point your phone at this screen to capture the QR code</span>"
        )

        instructions.setAlignment(Qt.AlignLeft)
        instructions.setWordWrap(True)
        instructions.setFont(QFont("Arial", 10))
        instructions.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        instructions.setStyleSheet("padding-left: 30px; line-height: 35px;")

        h_layout.addWidget(instructions)
       
        spacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        h_layout.addSpacerItem(spacer)

        # Link Label
        link_label = BodyLabel('<a href="#">Link with phone number</a>')
        link_label.setAlignment(Qt.AlignLeft)
        link_label.setFont(QFont("Arial", 9, QFont.Bold))
        link_label.setOpenExternalLinks(False)
        link_label.linkActivated.connect(self.show_third_page)  

        link_label.setStyleSheet("padding-left: 33px;")  
        h_layout.addWidget(link_label)

        qr_label = QLabel(self.second_page)
        pixmap = QPixmap("qr2.png")  
        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignCenter) 
        qr_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        h_combined_layout = QHBoxLayout()
        h_combined_layout.addLayout(h_layout, stretch=0) 
        h_combined_layout.addWidget(qr_label, stretch=3)

        central_layout.addLayout(h_combined_layout)

        central_layout.addStretch(1)

        outer_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        outer_layout.addStretch(1)  
    
    def init_third_page(self):
        """Initialize the third page"""
        outer2_layout = QVBoxLayout(self.third_page)  # Directly set the layout to the page

        central2_frame = QFrame(self.third_page)
        central2_frame.setStyleSheet("background-color: white; border-radius: 10px;")
        central2_frame.setFixedSize(900, 600)
        
        central2_layout = QVBoxLayout(central2_frame)
        
        central2_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        spacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)  # adjust height as needed
        central2_layout.addItem(spacer)



        label = BodyLabel("Enter phone number", central2_frame)
        label.setFont(QFont("Arial", 11))
        label.setAlignment(Qt.AlignCenter)
        central2_layout.addWidget(label)


        central2_layout.addStretch(1)
        central2_layout.addSpacing(10)


        label2 = BodyLabel("Select a country and your WhatsApp phone number", central2_frame)
        label2.setFont(QFont("Arial",11))
        label2.setAlignment(Qt.AlignCenter)
        central2_layout.addWidget(label2)
        central2_layout.addStretch(17)
                
        button = DropDownPushButton( 'Select contry/region')

        menu = RoundMenu(parent=button)

        search_box = QLineEdit(menu)
        search_box.setPlaceholderText("search contry/region")

        menu.setFixedSize(200,100)
        menu.layout().addWidget(search_box)
        central2_layout.setAlignment(search_box,Qt.AlignCenter)

        menu.addAction(Action(FluentIcon.BASKETBALL, 'Basketball', triggered=lambda: print("What are you doing?")))
        menu.addAction(Action(FluentIcon.ALBUM, 'Sing', triggered=lambda: print("I like singing, rapping, and dancing")))
        menu.addAction(Action(FluentIcon.MUSIC, 'Music', triggered=lambda: print("Just because you are so beautiful")))

        button.setMenu(menu)

        button.setFixedSize(195,40)
        central2_layout.addWidget(button)
        central2_layout.setAlignment(button,Qt.AlignCenter)

        central2_layout.addStretch(150)
        
        outer2_layout.addStretch(1)
        outer2_layout.addWidget(central2_frame, alignment=Qt.AlignCenter)
        outer2_layout.addStretch(1)

        self.third_page.setLayout(outer2_layout) 

    def show_third_page(self):
        """Switch to the third page when link is clicked"""
        self.central_widget.setCurrentWidget(self.third_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
