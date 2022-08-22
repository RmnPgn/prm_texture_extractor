import os.path

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
import func_extract_textures_list
import func_copy_needed_textures


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # setting up variables
        self.project_root = ""
        self.project_destination = ""
        self.maya_scene = ""
        self.texture_list = []
        self.number_of_textures = 0.0

        # setting up the core widget
        main_layout = QGridLayout()
        self.setLayout(main_layout)

        self.setWindowTitle("Texture extractor 0.1")
        self.setMinimumSize(QSize(300, 350))
        self.resize(QSize(700, 350))
        main_layout.setContentsMargins(10, 10, 10, 10)

        # creates widgets from modules
        self.input_module_elements = ui_modules.inputs_module()
        self.visu_module_elements = ui_modules.visualization_module()
        self.copy_module_elements = ui_modules.copy_module()
        self.info_module_elements = ui_modules.informations_module()

        # implement widgets to the core widget
        main_layout.addWidget(self.input_module_elements["widget"], 1, 1)
        main_layout.addWidget(self.visu_module_elements["widget"], 2, 1)
        main_layout.addWidget(self.copy_module_elements["widget"], 3, 1)
        main_layout.addWidget(self.info_module_elements["widget"], 4, 1)

        # link the buttons to their respective functions
        self.input_module_elements["project_root_button"].clicked.connect(
            self.interact_for_project_root_button
        )
        self.input_module_elements["destination_button"].clicked.connect(
            self.interact_for_destination_button
        )
        self.input_module_elements["maya_scene_button"].clicked.connect(
            self.interact_for_maya_scene_button
        )
        self.visu_module_elements["button"].clicked.connect(
            self.interact_visualisation_button
        )
        self.copy_module_elements["button"].clicked.connect(
            self.interact_copy_button
        )

    def interact_for_project_root_button(self):
        """
        The action when the "project root" button is pressed.
        Opens the directory browser, and updates the project root line edit when directory has been chosen.
        """
        self.project_root = func_open_file_dialog.open_directory_dialog("Select project root", "")
        func_change_text_line_edit.change_text_line_edit(
            self.input_module_elements["project_root_line_edit"],
            self.project_root
        )

    def interact_for_destination_button(self):
        """
        The action when the "destination" button is pressed.
        Opens the directory browser, and updates the destination line edit when directory has been chosen.
        """
        self.project_destination = func_open_file_dialog.open_directory_dialog("Select destination folder", "")
        func_change_text_line_edit.change_text_line_edit(
            self.input_module_elements["destination_line_edit"],
            self.project_destination
        )

    def interact_for_maya_scene_button(self):
        """
        The action when the "maya scene" button is pressed.
        Opens the file brower, and updates the maya scene line edit when the file has been chosen.
        """
        self.maya_scene = func_open_file_dialog.open_file_dialog("Select maya scene", "")
        func_change_text_line_edit.change_text_line_edit(
            self.input_module_elements["maya_scene_line_edit"],
            self.maya_scene
        )

    def interact_visualisation_button(self):
        """
        The action when the visualisation button is pressed.
        If the path exists, finds and displays all the textures that are going to be copied.
        """
        maya_scene_path = self.input_module_elements["maya_scene_line_edit"].text()
        if maya_scene_path != "" \
                and os.path.exists(maya_scene_path):
            if maya_scene_path.endswith(".ma") \
                    or maya_scene_path.endswith(".ma\\") \
                    or maya_scene_path.endswith(".ma/"):
                self.texture_list = func_extract_textures_list.extract_texture_paths_from_scene(
                    self.input_module_elements["maya_scene_line_edit"].text()
                )
                self.number_of_textures = len(self.texture_list)
                self.visu_module_elements["list_widget"].clear()
                for texture in self.texture_list:
                    self.visu_module_elements["list_widget"].addItem(texture)
                self.change_info_label_message(
                    str(self.number_of_textures)
                    + " files are going to be copied."
                )
            else:
                print("The file must be an ASCII file.")
                self.change_info_label_message("The file must be an ASCII file.")
        else:
            print("The maya scene location path is blank or incorrect.")
            self.change_info_label_message("The maya scene location path is blank or incorrect.")

    def interact_copy_button(self):
        """
        The action when the copy button is pressed.
        If file path exist, copy all the textures to the destination.
        If the destination path does not exist, it will be created.
        The progress bar will display the advance of the function.
        """
        project_root = self.input_module_elements["project_root_line_edit"].text()
        destination_path = self.input_module_elements["destination_line_edit"].text()
        copy_progression = 0.0

        self.change_progress_bar_value(copy_progression)

        if project_root != "" \
                and os.path.exists(project_root):
            if destination_path != "" \
                    and os.path.exists(destination_path):
                for texture in self.texture_list:
                    try:
                        #func_copy_needed_textures.copy_needed_textures(texture, project_root, destination_path)
                        copy_progression += 1.0
                        copy_ratio = (copy_progression / float(self.number_of_textures))*100

                        self.change_progress_bar_value(copy_ratio)

                    except:
                        self.change_info_label_message("An error occured.")
                        pass
                self.change_info_label_message("All the " + str(int(self.number_of_textures)) +
                                               " texture files have been copied properly.")
            else:
                self.change_info_label_message("The destination path is blank or incorrect.")
        else:
            self.change_info_label_message("The project root is blank or incorrect.")

    def change_info_label_message(self, new_message):
        """
        Changes the info label with a new message.
        :param str new_message:
        :return:
        """
        self.info_module_elements["info_label"].setText(new_message)

    def change_progress_bar_value(self, new_value):
        """
        Changes progress bar value
        :param float new_value:
        :return:
        """
        self.copy_module_elements["progress_bar"].setValue(new_value)
