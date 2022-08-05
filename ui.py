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
                                QListWidget
                               )
from PySide2.QtCore import QSize, Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QGridLayout()
        self.setLayout(main_layout)

        self.setMinimumSize(QSize(400, 100))
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setHorizontalSpacing(5)

        project_root_label = QLabel("Project root : ")
        project_root_line_edit = QLineEdit()
        project_root_button = QPushButton("Explorer")

        maya_scene_label = QLabel("Project root : ")
        maya_scene_line_edit = QLineEdit()
        maya_scene_button = QPushButton("Explorer")

        destination_label = QLabel("Destination path : ")
        destination_line_edit = QLineEdit()
        destination_button = QPushButton("Explorer")

        previsualization_button = QPushButton("Previsualization")
        launch_button = QPushButton("Launch transfer")
        list_widget = QListWidget()

        main_layout.addWidget(project_root_label, 1, 1, 1, 1)
        main_layout.addWidget(project_root_line_edit, 1, 2, 1, 1)
        main_layout.addWidget(project_root_button, 1, 3, 1, 1)

        main_layout.addWidget(maya_scene_label, 2, 1, 1, 1)
        main_layout.addWidget(maya_scene_line_edit, 2, 2, 1, 1)
        main_layout.addWidget(maya_scene_button, 2, 3, 1, 1)

        main_layout.addWidget(destination_label, 3, 1, 1, 1)
        main_layout.addWidget(destination_line_edit, 3, 2, 1, 1)
        main_layout.addWidget(destination_button, 3, 3, 1, 1)

        main_layout.addWidget(previsualization_button, 4, 1, 1, 3)
        main_layout.addWidget(list_widget, 5, 1, 1, 3)
        main_layout.addWidget(launch_button, 6, 1, 1, 3)