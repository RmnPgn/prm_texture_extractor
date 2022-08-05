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
import func_open_file_dialog
import func_change_text_line_edit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.project_root = ""
        self.project_destination = ""
        self.maya_scene = ""

        main_layout = QGridLayout()
        self.setLayout(main_layout)

        self.setWindowTitle("Texture extractor 0.1")
        self.setMinimumSize(QSize(300, 350))
        self.resize(QSize(700,350))
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.input_module_elements = ui_modules.inputs_module()
        visu_widget = ui_modules.visualization_module()
        copy_widget = ui_modules.copy_module()
        info_widget = ui_modules.informations_module()

        main_layout.addWidget(self.input_module_elements["widget"], 1, 1)
        main_layout.addWidget(visu_widget, 2, 1)
        main_layout.addWidget(copy_widget, 3, 1)
        main_layout.addWidget(info_widget, 4, 1)

        self.input_module_elements["project_root_button"].clicked.connect(
            self.interact_for_project_root_button
        )
        self.input_module_elements["destination_button"].clicked.connect(
            self.interact_for_destination_button
        )
        self.input_module_elements["maya_scene_button"].clicked.connect(
            self.interact_for_maya_scene_button
        )


    def interact_for_project_root_button(self):
        self.project_root = func_open_file_dialog.open_file_dialog("Select project root", "")
        func_change_text_line_edit.change_text_line_edit(
            self.input_module_elements["project_root_line_edit"],
            self.project_root
        )

    def interact_for_destination_button(self):
        self.project_destination = func_open_file_dialog.open_file_dialog("Select destination folder", "")
        func_change_text_line_edit.change_text_line_edit(
            self.input_module_elements["destination_line_edit"],
            self.project_destination
        )

    def interact_for_maya_scene_button(self):
        self.maya_scene = func_open_file_dialog.open_file_dialog("Select maya scene", "")
        func_change_text_line_edit.change_text_line_edit(
            self.input_module_elements["maya_scene_line_edit"],
            self.maya_scene
        )

