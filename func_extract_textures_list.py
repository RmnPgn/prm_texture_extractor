import os


def extract_texture_paths_from_scene(maya_scene_source_path):
    """
    Open the maya file and extract the path of the needed textures.

    :param str maya_scene_source_path:
    :return: A list of the texture path needed for the project.
    :rtype: list
    """
    maya_scene_source_path = maya_scene_source_path.replace('/', '\\')
    scene_file = open(maya_scene_source_path)
    scene_text_list = scene_file.readlines()
    scene_file.close()

    texture_path_list = []

    for text_line in scene_text_list:
        if text_line.startswith('	setAttr ".filename" -type "string"'):
            if "sourceimages" in text_line:
                if 'udim' in text_line:
                    texture_directory = text_line.split('	setAttr ".filename" -type "string" ')[-1].replace("\"", "")\
                        .replace(";", "").replace("/", "\\").rstrip().lstrip().replace("\\\\sourceimages", "\\sourceimages")
                    cropped_directory = (texture_directory.split("\\"))
                    cropped_directory.pop(-1)
                    cropped_directory = '\\'.join(cropped_directory)
                    dir_content = os.listdir(cropped_directory)
                    for texture in dir_content:
                        texture_name = texture.split(".")[0]
                        target_texture_name = texture_directory.split('\\')[-1].split('.')[0]
                        if texture_name == target_texture_name and texture_name != "":
                            texture_path_list.append(cropped_directory+'\\'+texture)
                elif '<u>' in text_line or '<v>' in text_line or '<U>' in text_line or '<V>' in text_line:
                    texture_directory = text_line.split('	setAttr ".filename" -type "string" ')[-1].replace("\"", "")\
                        .replace(";", "").replace("/", "\\").rstrip().lstrip().replace("\\\\sourceimages", "\\sourceimages")
                    cropped_directory = (texture_directory.split("\\"))
                    cropped_directory.pop(-1)
                    cropped_directory = '\\'.join(cropped_directory)
                    dir_content = os.listdir(cropped_directory)
                    for texture in dir_content:
                        texture_name = texture
                        target_texture_name = texture_directory.split('\\')[-1].split("_u<u>_v<v>_")[0]
                        if target_texture_name in texture_name and texture_name != "":
                            texture_path_list.append(cropped_directory+'\\'+texture)

                elif 'udim' not in text_line:
                    line_text = text_line.split('	setAttr ".filename" -type "string" ')[-1].replace("\"", "")\
                        .replace(";", "").replace("/", "\\").rstrip().lstrip().replace("\\\\sourceimages", "\\sourceimages")
                    texture_path_list.append(line_text)

    return texture_path_list
