import os
import shutil
import func_test_path


def copy_needed_textures(texture, project_root, destination_root):
    """
    Copy and paste the textures at the right place.

    Modules required :
    functions.test_path()

    :param str texture:
    :param str project_root :
    :param str destination_root:
    :return: A list of all the files copied.
    :rtype list
    """

    destination_path = texture.lower().replace(project_root.lower(), destination_root)

    path_to_test = destination_path.split("\\")
    path_to_test.pop(-1)
    func_test_path.test_path(path_to_test)

    texture_final_path = "\\".join(path_to_test)+"\\"+texture.split("\\")[-1]

    if os.path.exists('\\'.join(path_to_test)):
        shutil.copy(texture, texture_final_path)

