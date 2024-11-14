from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from time import sleep
import sys
from PyQt5.QtCore import Qt,QThread
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from qfluentwidgets import PrimaryPushButton, LineEdit

class Automationworker(QThread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()
        try:
            google_search = WebDriverWait(driver,20).until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
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
        self.setStyleSheet("background: rgb(225,225,225);")  

    def init_ui(self):
        self.resize(900, 600)

        layout = QVBoxLayout(self)
        layout.addStretch(1) 
        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("example@example.com")
        self.lineEdit.setText("")
        print(self.lineEdit.text())
    
        self.lineEdit.setClearButtonEnabled(True)
        layout.addWidget(self.lineEdit,alignment= Qt.AlignCenter)

        button = PrimaryPushButton("push button")
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
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())
