import os
import shutil

if __name__ == "__main__":

    path_to_valid_txt = r"D:\Pycharm_Projects\Make_model_with_YOLO\imgs\joined_bolts\valid.txt"
    destination_folder = r"D:\Pycharm_Projects\GIT_diplom\diplom\imgs\VALID_DATASET"
    paths = []

    # копируем фото
    with open(path_to_valid_txt, "r") as file:
        for row in file.readlines():
            paths.append(row.rstrip())

    print(*paths)
    for file in paths:
        shutil.copy(file, destination_folder)

    paths_to_txt = []
    # копируем txt файлы
    for row in paths:
        name_of_txt = row[:-4] if row.endswith('jpeg') else row[:-3]
        name_of_txt += "txt"
        paths_to_txt.append(name_of_txt)

    for file in paths_to_txt:
        shutil.copy(file, destination_folder)

