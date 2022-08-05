import os
import shutil
import func_test_path
def copy_needed_textures(texture_to_copy_list, project_root, destination_root):
    """
    Copy and paste the textures at the right place.

    Modules required :
    functions.test_path()

    :param list texture_to_copy_list:
    :param str project_root :
    :param str destination_root:
    :return: A list of all the files copied.
    :rtype list
    """
    all_copied_files = []
    for texture in texture_to_copy_list:
        destination_path = texture.lower().replace(project_root.lower(), destination_root)
        all_copied_files.append(destination_path)

        path_to_test = destination_path.split("\\")
        path_to_test.pop(-1)
        func_test_path.test_path(path_to_test)

        texture_final_path = "\\".join(path_to_test)+"\\"+texture.split("\\")[-1]

        if os.path.exists('\\'.join(path_to_test)):
            shutil.copy(texture, texture_final_path)

    return all_copied_files