import os


def test_path(path_to_test):
    """
    Test if the path is existing. If not, create the missing folders.

    :param list path_to_test:
    :return:
    :rtype bool
    """
    existing_path = ""
    for folder in path_to_test:
        if folder == "":
            existing_path = existing_path+'\\'
        else:
            new_path = existing_path+folder
            if os.path.exists(new_path):
                existing_path = existing_path+folder+'\\'
            elif new_path == "\\\\storage" \
                    or new_path == "//storage" \
                    or new_path == "\\\\Storage" \
                    or new_path == "//Storage":
                existing_path = existing_path+folder+'\\'
            else:
                os.mkdir(new_path)
                existing_path = existing_path+folder+'\\'
