from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from qfluentwidgets import PrimaryPushButton, LineEdit

driver = webdriver.Chrome()
driver.get("www.google.com")

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setStyleSheet("background: rgb(225,225,225);")  # बैकग्राउंड रंग सेट किया गया

    def init_ui(self):
        self.resize(900, 600)

        # Main layout for the window
        layout = QVBoxLayout(self)

        layout.addStretch(3)

        # LineEdit
        lineEdit = LineEdit()
        lineEdit.setPlaceholderText("example@example.com")
        lineEdit.setText("shokokawaii@foxmail.com")
        print(lineEdit.text())
        lineEdit.setClearButtonEnabled(True)
        layout.addWidget(lineEdit,alignment= Qt.AlignCenter)
      
        # Add stretch above the button to center it vertically

        # Button
        button = PrimaryPushButton("push button")
        button.setFixedSize(150, 40)  # Optional: Set a fixed size for the button
        layout.addWidget(button, alignment=Qt.AlignCenter)

        # Add stretch below the button to center it vertically
        layout.addStretch(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())
