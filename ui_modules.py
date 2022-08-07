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
from PySide2.QtCore import Qt
import ui


def inputs_module():
    """
    Create the widget with all the inputs for the UI.
    :return: Widget with all the inputs fields.
    :rtype QWidget
    """
    input_widget = QWidget()
    input_layout = QGridLayout()
    input_widget.setLayout(input_layout)

    project_root_label = QLabel("Project root : ")
    project_root_line_edit = QLineEdit()
    project_root_button = QPushButton("Explorer")

    maya_scene_label = QLabel("Maya ASCII scene : ")
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

    input_module_dict = {
                         "widget": input_widget,
                         "project_root_button": project_root_button,
                         "project_root_line_edit": project_root_line_edit,
                         "destination_line_edit": destination_line_edit,
                         "destination_button": destination_button,
                         "maya_scene_line_edit": maya_scene_line_edit,
                         "maya_scene_button": maya_scene_button
                        }

    return input_module_dict


def visualization_module():
    """
    Create the widget for the previsualization for the UI.
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

    visu_module_dict = {
        "widget":visu_widget,
        "button":visualization_button,
        "list_widget":list_widget
    }

    return visu_module_dict


def copy_module():
    """
    Create the copy widget of the UI.
    :return: Widget with the copy button and the waiting bar.
    :rtype QWidget
    """
    copy_widget = QWidget()
    copy_layout = QVBoxLayout()
    copy_widget.setLayout(copy_layout)

    copy_progress_bar = QProgressBar()
    launch_button = QPushButton("Launch transfer")

    copy_progress_bar.setValue(0)

    copy_layout.addWidget(copy_progress_bar)
    copy_layout.addWidget(launch_button)

    copy_module_dict = {
        "widget":copy_widget,
        "progress_bar":copy_progress_bar,
        "button":launch_button
    }

    return copy_module_dict


def informations_module():
    """
    Create the information module of the UI.
    :return: The information widget
    :rtype QWidget
    """
    informations_widget = QWidget()
    informations_layout = QGridLayout()
    informations_widget.setLayout(informations_layout)

    info_label = QLabel("Informations will display here")

    informations_layout.addWidget(info_label, 1, 1, Qt.AlignCenter)

    informations_module_dict = {
        "widget":informations_widget,
        "info_label":info_label
    }

    return informations_module_dict
