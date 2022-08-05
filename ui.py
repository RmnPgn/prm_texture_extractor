from PySide2.QtWidgets import (
                                QApplication,
                                QWidget,
                                QMainWindow,
                                QPushButton,
                                QVBoxLayout,
                                QFileDialog,
                                QGridLayout,
                                QLineEdit,
                                QLabel,
                                QListWidget,
                                QProgressBar
                               )
from PySide2.QtCore import QSize, Qt
import ui_modules

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QGridLayout()
        self.setLayout(main_layout)

        self.setWindowTitle("Texture extractor 0.1")
        self.setMinimumSize(QSize(300, 350))
        main_layout.setContentsMargins(10, 10, 10, 10)

        input_widget = ui_modules.inputs_module()
        visu_widget = ui_modules.visualization_module()
        copy_widget = ui_modules.copy_module()
        info_widget = ui_modules.informations_module()

        main_layout.addWidget(input_widget, 1, 1)
        main_layout.addWidget(visu_widget, 2, 1)
        main_layout.addWidget(copy_widget, 3, 1)
        main_layout.addWidget(info_widget, 4, 1)
