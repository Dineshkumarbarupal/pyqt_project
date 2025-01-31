# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QEventLoop, QTimer, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from qfluentwidgets import SplashScreen
from qframelesswindow import FramelessWindow, StandardTitleBar

class Demo(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle('PyQt-Fluent-Widgets')
        self.setWindowIcon(QIcon('C:\\Users\\NSG\\Desktop\\qfluent widget\\whatsapp3-removebg-preview.png'))
        
        # create splash screen and show window
        self.splashscreen = SplashScreen(self.windowIcon(), self)
        self.splashscreen.setIconSize(QSize(333,333))
        self.splashscreen.show()

        # customize the title bar of splash screen
        # titleBar = StandardTitleBar(self.splashScreen)
        # titleBar.setIcon(self.windowIcon())
        # titleBar.setTitle(self.windowTitle())
        # self.splashScreen.setTitleBar(titleBar)

        self.show()

        # create other subinterfaces
        self.createSubInterface()

        # close splash screen
        self.splashscreen.finish()
     
    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(3000,loop.quit)
        loop.exec()
              
        
if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()