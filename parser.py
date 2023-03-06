import requests
from bs4 import BeautifulSoup
import re
import json
import urllib.request
import vk_api
import vk_api.longpoll
import vk_api.utils
# from vk_api.longpoll import VkLongPoll, VkEventType
# from vk_api.utils import get_random_id
import time


# Получаем данные из поисковиков с задаваемой тематики
def get_data_from_search_engines(query):
    # Получаем данные с google
    google_url = 'https://www.google.com/search?q=' + query + '&num=10'
    response = requests.get(google_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получаем данные с yandex
    yandex_url = 'https://yandex.ru/search/?text=' + query + '&numdoc=10'
    response = requests.get(yandex_url)
    soup2 = BeautifulSoup(response.text, 'html.parser')

    # Сохраняем данные в словарь
    data = {'google': [], 'yandex': []}

    # Получаем ссылки с google
    for g in soup.find_all('div', class_='r'):
        link = g.find('a')['href']
        data['google'].append(link)

    # Получаем ссылки с yandex
    for y in soup2.find_all('div', class_='organic__url-text'):
        link = y.find('a')['href']
        data['yandex'].append(link)

    return data


# Получаем данные из групп Вконтакте с задаваемой тематики
def get_data_from_vk(query):
    # Авторизуемся в VK API
    vk_session = vk_api.VkApi(token='YOUR TOKEN')

    # Получаем список групп с VK API
    vk = vk_session.get_api()

    groups = vk.groups.search(q=query, count=10)

    # Сохраняем данные в словарь
    data = {'vk': []}

    # Получаем ссылки на группы
    for g in groups['items']:
        link = 'https://vk.com/' + g['screen_name']
        data['vk'].append(link)

    return data


# Сохраняем данные в структурированном виде
def save_data(data):
    # Сохраняем данные в файл
    with open('data.json', 'w') as f:
        json.dump(data, f)


# Публикуем данные на сайте с движком wordpress
def publish_data(data):
    # Авторизуемся на сайте с wordpress
    url = 'YOUR URL'
    username = 'YOUR USERNAME'
    password = 'YOUR PASSWORD'

    # Формируем словарь с данными для POST-запроса
    payload = {'log': username, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': url}

    # Отправляем POST-запрос
    with requests.Session() as s:
        p = s.post(url, data=payload)

        # Проверяем, что авторизация прошла успешно
        if p.status_code == 200:

            # Формируем словарь с данными для POST-запроса
            payload = {'post_title': data['title'], 'post_content': data['content']}

            # Отправляем POST-запрос
            r = s.post(url, data=payload)

            # Проверяем, что POST-запрос был успешно
            if r.status_code == 200:
                print('Data published successfully!')

            else:
                print('Error publishing data!')

        else:
            print('Error logging in!')


# Главная функция
def main():
    query = 'YOUR QUERY'

    # Получаем данные из поисковиков
    data_from_search_engines = get_data_from_search_engines(query)

    # Получаем данные из групп Вконтакте
    data_from_vk = get_data_from_vk(query)

    # Объединяем данные
    data = {**data_from_search_engines, **data_from_vk}

    # Сохраняем данные
    save_data(data)

    # Публикуем данные
    publish_data(data)


if __name__ == '__main__':
    main()
