from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QSize, QEventLoop
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, SplashScreen
from qframelesswindow import FramelessWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from time import sleep
import sys

class Automationworker(QThread):
    text_extracted = pyqtSignal(str) # Signal to emit extracted text

    def __init__(self, url,search):
        super().__init__()
        self.url = url
        self.search = search
    def run(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()

        try:
            google_search = WebDriverWait(driver, 20).until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
            google_search.send_keys(self.search)
            google_search.send_keys(Keys.ENTER)

            w3schools_link = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
            w3schools_link.click()

            self.text = WebDriverWait(driver,10).until(Ec.presence_of_element_located((By.CLASS_NAME,'learntocodeh1'))).text

            print(self.text)
            self.text_extracted.emit(self.text)  # Emit the text
            
            screenshot_path = "screenshot.png"
            driver.save_screenshot(screenshot_path)
            print(f"screenshot saved in {screenshot_path}")    
        except Exception as e:
            print("An error occurred...", e)

        sleep(30)
        driver.quit()

class Mainwindow(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle('Automation')
        self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\automation.png'))

        # create splash screen and show window
        splashScreen = SplashScreen(self.windowIcon(), self)
        splashScreen.setIconSize(QSize(150, 150))
        self.show()
        self.createSubInterface()
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

        self.lineEdit3 = LineEdit()
        self.lineEdit3.setPlaceholderText("Sereach Something.")
        layout.addWidget(self.lineEdit3,alignment=Qt.AlignCenter)

        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("https://www.example.com")
        layout.addWidget(self.lineEdit, alignment=Qt.AlignCenter)

        self.lineEdit2 = LineEdit()
        self.lineEdit2.setPlaceholderText("Extracted text will appear here")
        layout.addWidget(self.lineEdit2, alignment=Qt.AlignCenter)
        
        layout.addSpacing(8)
        button = PrimaryPushButton("Start")
        button.setFixedSize(130, 30) 
        layout.addWidget(button, alignment=Qt.AlignCenter)
        button.clicked.connect(self.automation)

        layout.addStretch(3)

    def automation(self):
        url = self.lineEdit.text()
        search = self.lineEdit3.text()
        if url:
            self.worker = Automationworker(url,search)
            self.worker.text_extracted.connect(self.display_text)  # Connect signal to slot
            self.worker.start()
        else:
            print("Please enter a valid URL.")

    def display_text(self, text):
        """Update lineEdit2 with extracted text once thread finishes."""
        self.lineEdit2.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())
