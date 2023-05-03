from sys import argv
import re


# замена anchors в файле
def zamena_anchors(file_path, anchors):
    text = ""
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.readlines()

    indexes_to_rewrite = []
    for idx, line in enumerate(text):
        if "anchors" in line:
            indexes_to_rewrite.append(idx)

    for i in indexes_to_rewrite:
        text[i] = anchors

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(text)


#### Здесь я делаю замену anchors в конфигах


if __name__ == "__main__":
    # # file_path = argv[1]
    # # anchors = argv[2]
    # anchors = "anchors =  68, 84,  62,183, 163,127, 129,273, 274,205, 365,352 \n"
    # file_path = r"C:\Users\Admin\PycharmProjects\Make_model_with_YOLO\backups\cfgs\bolt_test.cfg"


    params = argv[1:]
    file_to_anchors, file_path_to_test, file_path_to_train = params

    anchors = ""
    with open(file_to_anchors, "r", encoding="utf-8") as file:
        anchors = file.readline().strip("\n")
    anchors += "\n"
    # заменяем конфиг
    zamena_anchors(file_path_to_test, anchors)
    zamena_anchors(file_path_to_train, anchors)





