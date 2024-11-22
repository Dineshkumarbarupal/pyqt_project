from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QSize, QEventLoop
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QStackedWidget
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
    text_extracted = pyqtSignal(str)

    def __init__(self, url, search):
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

            self.text = WebDriverWait(driver, 10).until(Ec.presence_of_element_located((By.CLASS_NAME, 'learntocodeh1'))).text

            print(self.text)
            self.text_extracted.emit(self.text)

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

        splashScreen = SplashScreen(self.windowIcon(), self)
        splashScreen.setIconSize(QSize(150, 150))
        self.createSubInterface()
        splashScreen.finish()

    def createSubInterface(self):
        self.central_widget = QStackedWidget(self)  # QStackedWidget for multiple pages
        self.setLayout(QVBoxLayout())  # Main layout for the FramelessWindow
        self.layout().addWidget(self.central_widget)
        
        # Add the first page
        self.main_page = QWidget()
        main_layout = QVBoxLayout(self.main_page)

        label = BodyLabel("Enter website which you want to automate")
        main_layout.addWidget(label, alignment=Qt.AlignCenter)

        main_layout.addSpacing(5)

        self.lineEdit3 = LineEdit()
        self.lineEdit3.setPlaceholderText("Search Something.")
        main_layout.addWidget(self.lineEdit3, alignment=Qt.AlignCenter)

        self.lineEdit4 = LineEdit()
        self.lineEdit4.setPlaceholderText("Fill form")
        main_layout.addWidget(self.lineEdit4, alignment=Qt.AlignCenter)

        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("https://www.example.com")
        main_layout.addWidget(self.lineEdit, alignment=Qt.AlignCenter)

        self.lineEdit2 = LineEdit()
        self.lineEdit2.setPlaceholderText("Extracted text will appear here")
        main_layout.addWidget(self.lineEdit2, alignment=Qt.AlignCenter)

        main_layout.addSpacing(2)
        button = PrimaryPushButton("Start")
        button.setFixedSize(130, 30)
        main_layout.addWidget(button, alignment=Qt.AlignCenter)
        button.clicked.connect(self.automation)

        button2 = PrimaryPushButton("Next page")
        button2.setFixedSize(130, 30)
        button2.clicked.connect(self.next_page)
        main_layout.addWidget(button2, alignment=Qt.AlignCenter)

        self.central_widget.addWidget(self.main_page)

    def automation(self):
        url = self.lineEdit.text()
        search = self.lineEdit3.text()
        if url:
            self.worker = Automationworker(url, search)
            self.worker.text_extracted.connect(self.display_text)
            self.worker.start()
        else:
            print("Please enter a valid URL.")

    def display_text(self, text):
        self.lineEdit2.setText(text)

    def next_page(self):
        # Create and add the second page
        second_page = Second_page()
        self.central_widget.addWidget(second_page)
        self.central_widget.setCurrentWidget(second_page)

class Second_page(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("This is the second page.")
        layout.addWidget(label, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mainwindow()
    w.show()
    sys.exit(app.exec_())



