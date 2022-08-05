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

        self.setWindowTitle("Texture extractor 0.1")
        self.setMinimumSize(QSize(400, 100))
        main_layout.setContentsMargins(10, 10, 10, 10)

        input_widget = inputs_module()
        visu_widget = visualization_module()
        copy_widget = copy_module()

        main_layout.addWidget(input_widget, 1, 1)
        main_layout.addWidget(visu_widget, 2, 1)
        main_layout.addWidget(copy_widget, 3, 1)


def inputs_module():
    """
    Create the widget with all the inputs.
    :return: Widget with all the inputs fields.
    :rtype QWidget
    """
    input_widget = QWidget()
    input_layout = QGridLayout()
    input_widget.setLayout(input_layout)

    project_root_label = QLabel("Project root : ")
    project_root_line_edit = QLineEdit()
    project_root_button = QPushButton("Explorer")

    maya_scene_label = QLabel("Project root : ")
    maya_scene_line_edit = QLineEdit()
    maya_scene_button = QPushButton("Explorer")

    destination_label = QLabel("Destination path : ")
    destination_line_edit = QLineEdit()
    destination_button = QPushButton("Explorer")

    input_layout.addWidget(project_root_label, 1, 1, 1, 1)
    input_layout.addWidget(project_root_line_edit, 1, 2, 1, 1)
    input_layout.addWidget(project_root_button, 1, 3, 1, 1)

    input_layout.addWidget(maya_scene_label, 2, 1, 1, 1)
    input_layout.addWidget(maya_scene_line_edit, 2, 2, 1, 1)
    input_layout.addWidget(maya_scene_button, 2, 3, 1, 1)

    input_layout.addWidget(destination_label, 3, 1, 1, 1)
    input_layout.addWidget(destination_line_edit, 3, 2, 1, 1)
    input_layout.addWidget(destination_button, 3, 3, 1, 1)

    input_layout.setHorizontalSpacing(4)
    input_layout.setVerticalSpacing(2)

    return input_widget


def visualization_module():
    """
    Create the widget for the previsualization.
    :return: Widget with the visualization informations
    :rtype QWidget
    """
    visu_widget = QWidget()
    visu_layout = QVBoxLayout()
    visu_widget.setLayout(visu_layout)

    visualization_button = QPushButton("Show textures which will be copied")
    list_widget = QListWidget()

    visu_layout.addWidget(visualization_button)
    visu_layout.addWidget(list_widget)

    return visu_widget


def copy_module():
    """
    Create the copy widget.
    :return: Widget with the copy button and the waiting bar.
    :rtype QWidget
    """
    copy_widget = QWidget()
    copy_layout = QVBoxLayout()
    copy_widget.setLayout(copy_layout)

    launch_button = QPushButton("Launch transfer")

    copy_layout.addWidget(launch_button)

    return copy_widget
