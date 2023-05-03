import os
import os.path

if __name__ == "__main__":
    txt_files = []
    image_files = []

    path_to_directory = r"C:\Users\Admin\PycharmProjects\Make_model_with_YOLO\imgs\bolt"
    for file in os.listdir(path_to_directory):
        if file.endswith("jpg"):
            image_files.append(os.path.splitext(file)[0])
        elif file.endswith("txt"):
            txt_files.append(os.path.splitext(file)[0])

    txt_files_length = len(txt_files)
    image_files_length = len(image_files)

    print("Число текстовых файлов:", txt_files_length)
    print("Число файлов с изображениями: ", image_files_length)

    unrecognise_images = list((set(image_files).difference(set(txt_files))))  # неразмеченные файлы

    if unrecognise_images:
        print(*unrecognise_images, sep="\n")
        print("К удалению: ", len(unrecognise_images), "изображений")
        for file in unrecognise_images:
            os.remove(os.path.join(path_to_directory, file + ".jpg"))
        print(len(unrecognise_images), "изображений было успешно удалено")
    else:
        print("неразмеченных изображений нет", sep="\n")