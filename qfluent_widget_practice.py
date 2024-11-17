from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from time import sleep
import sys
from PyQt5.QtCore import Qt, QThread, QTimer, QSize, QEventLoop
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QSplashScreen
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel

class Automationworker(QThread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()

        try:
            google_search = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
            google_search.send_keys("w3school.com")
            google_search.send_keys(Keys.ENTER)

            w3schools_link = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
            w3schools_link.click()
        
            screenshot_path = "screenshot.png"
            driver.save_screenshot(screenshot_path)
            print(f"screenshot saved in {screenshot_path}")    
        except Exception as e:
            print("An error occurred...")

        sleep(30)
        driver.quit()

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setStyleSheet("background: rgb(001,225,225);")  
        self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\automation.png'))

    def init_ui(self):
        self.resize(900, 600)
        self.setWindowTitle('PyQt-Fluent-Widgets')
        self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp3-removebg-preview.png'))

        # create other subinterfaces
        self.createSubInterface()

    def createSubInterface(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1) 
        
        label = BodyLabel("Enter website which you want to automate")
        layout.addWidget(label, alignment=Qt.AlignCenter)

        layout.addSpacing(4)

        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("https://www.example.com")
        layout.addWidget(self.lineEdit, alignment=Qt.AlignCenter)
        
        layout.addSpacing(1)

        button = PrimaryPushButton("Start")
        button.setFixedSize(150, 40) 
        layout.addWidget(button, alignment=Qt.AlignCenter)
        button.clicked.connect(self.automation)

        layout.addStretch(3)

    def automation(self):
        url = self.lineEdit.text()
        if url:
            self.worker = Automationworker(url)
            self.worker.start()
        else:
            print("please enter a valid url....")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load and display splash screen
    pixmap = QPixmap('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp3-removebg-preview.png')
    splashScreen = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splashScreen.show()

    # Wait to simulate loading time (3 seconds)
    QTimer.singleShot(3000, splashScreen.close)  # Close after 3 seconds

    # Show main window
    w = Mainwindow()
    w.show()

    sys.exit(app.exec_())
