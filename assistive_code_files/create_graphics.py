from matplotlib import pyplot as plt
import random

if __name__ == "__main__":
    movies = ["1000", "2000"]
    movies = [str(i) + "%" + " от " + j for j in movies for i in range(10,16)]
    num_oscars = [69.61568891659621, 70.39102679744627, 71.87584699146313, 72.83745435213227, 73.83777429515568,
                  74.21453899107198, 70.21439945023792, 71.5305840418614, 72.79999590324907,
                  73.23328032988276, 74.97901031166886, 75.90646948180147]
    print(movies)
    print(len(num_oscars))
    # строим стобчатую диаграмму
    plt.bar(range(len(movies)), num_oscars)
    plt.title("Точность map при изменении размера тестового датасета")
    plt.ylabel("map")
    plt.xticks(range(len(movies)), movies, rotation=90)
    plt.show()