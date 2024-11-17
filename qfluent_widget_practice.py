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
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, SplashScreen
from qframelesswindow import FramelessWindow,StandardTitleBar

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

class Mainwindow(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        # self.setWindowTitle('Automation')
        self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\automation.png'))

        # create splash screen and show window
        splashScreen = SplashScreen(self.windowIcon(), self)
        splashScreen.setIconSize(QSize(150, 150))

        # customize the title bar of splash screen
        # titleBar = StandardTitleBar(self.splashScreen)
        # titleBar.setIcon(self.windowIcon())
        # titleBar.setTitle(self.windowTitle())
        # self.splashScreen.setTitleBar(titleBar)

        self.show()

        # create other subinterfaces
        self.createSubInterface()

        # close splash screen
        splashScreen.finish()

    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(3000, loop.quit)
        loop.exec()

        layout = QVBoxLayout(self)
        layout.addStretch(2) 
        
        label = BodyLabel("Enter website which you want to automate")
        layout.addWidget(label, alignment=Qt.AlignCenter)

        layout.addSpacing(10)

        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("https://www.example.com")
        layout.addWidget(self.lineEdit, alignment=Qt.AlignCenter)
        
        layout.addSpacing(8)
        button = PrimaryPushButton("Start")
        button.setFixedSize(130, 30) 
        layout.addWidget(button, alignment=Qt.AlignCenter)
        button.clicked.connect(self.automation)

        layout.addStretch(3)

    def automation(self):
        url = self.lineEdit.text()
        if url:
            self.worker = Automationworker(url)
            self.worker.start()
        else:
            print("please enter a valid url...")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Show main window
    w = Mainwindow()
    w.show()

    sys.exit(app.exec_())
