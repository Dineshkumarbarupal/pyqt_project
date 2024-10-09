import sys
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow,  QApplication, QVBoxLayout,QWidget
from qfluentwidgets import BodyLabel,HyperlinkLabel
 # from qfluentwidgets import 

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.resize(900,600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)


        label = BodyLabel("Label")
        label.setTextColor(QColor(0, 255, 0), QColor(255, 0, 0))  # Light theme, dark theme
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        layout.addSpacing(40)

        label2 = HyperlinkLabel(QUrl('https://github.com/'), 'GitHub')
        # hyperlinkLabel.setUnderlineVisible(True)
        label2.setUrl('https://github.com/zhiyiYo/QMaterialWidgets')
        layout.addWidget(label2)
        layout.setAlignment(Qt.AlignCenter)
        print(label2.url)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())



