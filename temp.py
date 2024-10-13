import sys
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import CalendarPicker, FluentTranslator

app = QApplication(sys.argv)
app.resize()

# create an translator instance that has the same lifecycle as the app
translator = FluentTranslator()
app.installTranslator(translator)

w = CalendarPicker()
w.show()
app.exec()
