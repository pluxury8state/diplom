from matplotlib import pyplot as plt
import random
import numpy
import matplotlib.patches as patches

if __name__ == "__main__":
    # полученные данные
    movies = ["датасет на 1000 фото", "датасет на 2000 фото"]
    # movies = [str(i) + "%" + " от " + j for j in movies for i in range(10, 20)]
    # maps = [69.61568891659621, 70.39102679744627, 71.87584699146313, 72.83745435213227, 73.83777429515568,
    #         74.21453899107198, 74.29726931128594, 74.3326834852581, 74.45418574993583, 74.58624321953582]
    maps = [96.11, 251.3]
    print(len(movies))
    print(len(maps))


    # строим стобчатую диаграмму
    fig, ax = plt.subplots(figsize=(16, 10), facecolor='white', dpi=90)

    # делаем подписи на барах
    for i, cty in enumerate(maps):
        ax.text(i, cty + 6.5, round(cty, 4), horizontalalignment='center', fontsize=14)
    plt.bar(range(len(movies)), maps, color=["green", "red"])

    # легенды
    plt.title("График времени обучения для наборов данных", fontsize=14)
    plt.ylabel("время, мин.", fontsize=14)

    # строим бары
    plt.xticks(range(len(movies)), movies, horizontalalignment='center', fontsize=14)

    # устанавливаем прямоугольники с подсветкой для положительных и отрицательных результатов
    # p2 = patches.Rectangle((.124, -0.02), width=.455, height=.13, alpha=.3, facecolor='green', transform=fig.transFigure)
    # p1 = patches.Rectangle((.58, -0.02), width=.33, height=.13, alpha=.3, facecolor='red', transform=fig.transFigure)
    # fig.add_artist(p1)
    # fig.add_artist(p2)

    # устанавливаем пределы по оси y
    plt.ylim([0, 320])

    # строим стрелки
    # plt.arrow(x=0, y=maps[5], dx=5, dy=0, width=.1, head_width=0.2)
    # plt.arrow(x=0, y=maps[0], dx=0, dy=maps[5] - maps[0], width=.001, head_width=0.001)
    # ax.annotate("", xy=(1+4, 2), xytext=(0, 0),
    #             arrowprops=dict(arrowstyle="->"))
    # показываем графики
    plt.show()