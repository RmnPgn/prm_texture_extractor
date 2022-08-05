def change_text_line_edit(object_name, text):
    """
    Change text line edit.
    :param QLineEdit object_name:
    :param str text:
    :return: New line edit text
    :rtype: str
    """
    object_name.setText(text)
    return text
