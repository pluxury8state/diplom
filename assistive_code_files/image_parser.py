# Здесь была описан скрипт, который скачивает картинки из интернета по определенному запросу
import os.path
from bs4 import BeautifulSoup as bs
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://yandex.ru/images/search?from=tabbar&text=человек%20картинки"
NAME_OF_OBJECT = "animals"
PATH_TO_DIRECTORY = os.path.join(r"C:\Users\Admin\PycharmProjects\Make_model_with_YOLO\imgs", NAME_OF_OBJECT)
PATH_TO_DOWNLOAD = os.path.join(PATH_TO_DIRECTORY, NAME_OF_OBJECT) + "-{}.jpg"
PATH_TO_TXT = os.path.join(PATH_TO_DIRECTORY, NAME_OF_OBJECT) + "_urls.txt"

# print(PATH_TO_DIRECTORY, PATH_TO_DOWNLOAD, PATH_TO_TXT, sep="\n")

SCROLL_PAUSE_TIME = 2  # время прогрузки страницы


def get_html(url, num_scrolls):

    driver = webdriver.Firefox()
    driver.get(url)

    count = 1  # счетчик

    last_height = driver.execute_script("return document.body.scrollHeight")

    while count != num_scrolls:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        try:
            btn = driver.find_element(By.LINK_TEXT, "Ещё картинки")
            btn.click()
            time.sleep(SCROLL_PAUSE_TIME)

        except Exception as e:
            if new_height == last_height:
                break

        finally:
            count += 1
            last_height = new_height
            print(count, "page")

    return driver.page_source


def get_exist_urls(path: str):
    list_of_urls = []
    num = 0
    with open(path, 'r', encoding="utf-8") as file:
        for num, line in enumerate(file.readlines()):
            list_of_urls.append(line.rstrip())
    return list_of_urls, num + 1


def remain_urls(path, new_urls):
    with open(path, 'a', encoding="utf-8") as file:
        for url in new_urls:
            file.write(url + "\n")


def parse_url(html):
    exist_urls = count = None
    new_urls = []
    try:
        exist_urls, count = get_exist_urls(PATH_TO_TXT)
    except FileNotFoundError as E:

        os.mkdir(PATH_TO_DIRECTORY)
        file = open(PATH_TO_TXT, 'w')
        file.close()
        exist_urls, count = [], 0

    soup = bs(html, "html.parser")
    images = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
    for img in images:
        link_to_download = "https:" + img["src"]
        if link_to_download in exist_urls:
            print("Эта картинка уже была:", link_to_download)
        else:
            print("Этой картинки еще не было:", link_to_download)
            wget.download(link_to_download, PATH_TO_DOWNLOAD.format(count))
            count += 1
            new_urls.append(link_to_download)

    remain_urls(PATH_TO_TXT, new_urls)


if __name__ == '__main__':
    parse_url(get_html(BASE_URL, 4))

