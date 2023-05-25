import os
import os.path

if __name__ == "__main__":
    txt_files = []

    path_to_directory = r"D:\Pycharm_Projects\GIT_diplom\diplom\imgs\nut"
    for file in os.listdir(path_to_directory):
        if file.endswith("txt"):
            path = os.path.join(path_to_directory, file)
            if os.path.getsize(path) == 0:
                txt_files.append(path)

    txt_files_length = len(txt_files)

    print("Число текстовых файлов на удаление :", txt_files_length)

    for file in txt_files:
        os.remove(file)

    print("Удалено") if txt_files_length else print("Нечего удалять...")
