import sys
from PySide2.QtWidgets import (QApplication)
import ui

app = QApplication(sys.argv)

window = ui.MainWindow()
window.show()

app.exec_()
