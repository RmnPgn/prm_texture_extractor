from PySide2.QtWidgets import (
                                QFileDialog
                              )


def open_file_dialog(window_name, default_location):
    """
    Open the browser to get the path of the selected files.
    :param str window_name:
    :param str default_location:
    :return:
    """
    file_name = QFileDialog.getOpenFileName(caption=window_name, dir=default_location)

    return file_name[0]
