from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from qfluentwidgets import PrimaryPushButton, LineEdit

def get_data():
    global link
    link = lineEdit.get()

def automation():
    driver = webdriver.Chrome()
    driver.get(link)

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setStyleSheet("background: rgb(225,225,225);")  

    def init_ui(self):
        self.resize(900, 600)

        layout = QVBoxLayout(self)
        layout.addStretch(3)
        global lineEdit   
        lineEdit = LineEdit()
        lineEdit.setPlaceholderText("example@example.com")
        lineEdit.setText("shokokawaii@foxmail.com")
        print(lineEdit.text())
        lineEdit.setClearButtonEnabled(True)
        layout.addWidget(lineEdit,alignment= Qt.AlignCenter)
      
     
        button = PrimaryPushButton("push button")
        button.setFixedSize(150, 40) 
        layout.addWidget(button, alignment=Qt.AlignCenter)
        button.clicked.connect(automation)

        layout.addStretch(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())