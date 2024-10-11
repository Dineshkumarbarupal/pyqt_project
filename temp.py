import sys
from PyQt5.QtCore import Qt, QDate, QTime,QEasingCurve,QUrl
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication,QPushButton
from qfluentwidgets import BodyLabel, Slider, SwitchButton, IconWidget, FluentIcon, DatePicker, TimePicker, CalendarPicker, ColorDialog,FlowLayout

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.setWindowIcon(QIcon('whatsapp_logo.ico'))  # Set your icon here
        self.resize(900, 700)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        slider = Slider(Qt.Horizontal)
        slider.setFixedWidth(200)

        # Set the value range and current value
        slider.setRange(0, 50)
        slider.setValue(20)

        layout.addWidget(slider)
        layout.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(central_widget)

        layout.addSpacing(50)

        button = SwitchButton()
        button.checkedChanged.connect(lambda checked: print("Is the button selected: ", checked))
        button.setChecked(True)
        print(button.isChecked())
        layout.addWidget(button)

        layout.addSpacing(50)

        w = IconWidget(FluentIcon.AIRPLANE)
        w.setFixedSize(20, 20)
        layout.addWidget(w)

        layout.addSpacing(50)

        datePicker = DatePicker()
        datePicker.setDate(QDate(2024, 10, 10))
        print(datePicker.date)
        datePicker.dateChanged.connect(lambda date: print(date.toString()))
        layout.addWidget(datePicker)

        timePicker = TimePicker()
        # Set the current time
        timePicker.setTime(QTime(13, 53, 26))
        # Get the current time
        print(timePicker.time)
        # Time changes
        timePicker.timeChanged.connect(lambda time: print(time.toString()))
        layout.addWidget(timePicker)

        calendarPicker = CalendarPicker()
        calendarPicker.setDate(QDate(2024, 2, 26))
        print(calendarPicker.date)
        calendarPicker.dateChanged.connect(lambda date: print(date.toString()))
        layout.addWidget(calendarPicker)

        # ColorDialog is used as a modal dialog, so we don't add it to the layout
        # colorDialog = ColorDialog(QColor(0, 255, 255), "Choose Background Color", central_widget, enableAlpha=False)
        # colorDialog.colorChanged.connect(lambda color: print("Selected color:", color.name()))
        # colorDialog.exec()


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        layout = FlowLayout(self, needAni=True)  # Enable animation

        # Custom animation parameters
        layout.setAnimation(250, QEasingCurve.OutQuad)

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setVerticalSpacing(20)
        layout.setHorizontalSpacing(10)

        layout.addWidget(QPushButton('aiko'))
        layout.addWidget(QPushButton('Liu Jingai'))
        layout.addWidget(QPushButton('Liu Ai Zi'))
        layout.addWidget(QPushButton('aiko Dai Suki'))
        layout.addWidget(QPushButton('aiko too love 😘'))

        self.resize(250, 300)
        
        from qfluentwidgets.multimedia import VideoWidget

        videoWidget = VideoWidget(self)

        videoWidget.setVideo(QUrl.fromLocalFile("D:/Video/aiko - シアワセ.mp4"))
        videoWidget.play()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    win = Demo()
    win.show()
    sys.exit(app.exec_())
