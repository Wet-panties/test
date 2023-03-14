import requests
from bs4 import BeautifulSoup
import re
import json
import time
import ast
import urllib.request
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

news_links = 'str'
topic = 'mra'
linkd = '123'

def link_pars():
    """
    Функция парсит ссылки и записывает их в файл result.txt
    """
    # Задаем тематику для поиска новостей
    global news_links
    global topic
    global linkd
    topic = 'фитнес'
    # Формируем ссылку для поиска новостей
    url = 'https://www.google.com/search?q=' + topic + '&source=lnt&tbs=lr:lang_1ru&lr=lang_ru'
    # Отправляем GET-запрос и получаем HTML-код страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # a = re.compile(r'\w{6}') print(soup) re.compile(pattern=r'\w{6}')
    # выражения описаны тут https://stackoverflow.com/questions/24748445/beautiful-soup-using-regex-to-find-tags

    # Ищем в HTML-коде ссылки на новости регулярные
    news_links = soup.find_all('a', {'class': re.compile(r'\w{6}')})
    # тестовый записатор новостных ссылок в файл result
    # with open('results.txt', 'w+') as f:
    #
    #     for linkd in soup.find_all('a'):
    #         linkse = linkd.get('href')
    #         if linkse.startswith('/url?q='):
    #             f.write(linkse[7:] + '\n')
    #     f.close()
    # return


link_pars()
print(type(news_links))

# with open('results.txt', 'r') as linkse:
#     # читаем все строки и удаляем переводы строк
#     urls = linkse.readlines()
#     urls = [line.rstrip('\n') for line in urls]
#     print(urls)
#     linkse.close()
#     # for i in linkse:
#     #     linkse = re.match()
#     #
#     # if linkse == '/sea'
#     #     with open('linkse.txt', 'w') as z:
#     #         z.write(linkse + '\n')
#     # with open('linkse.json', 'a') as f:
#     #     json.dump(linkse + '\n', f)

# Проходимся по каждой ссылке, чтобы получить HTML-код страницы с новостью
for link in news_links:
    news_url = link['href']  # Получаем URL-адрес новости
    news_response = requests.get(news_url)  # Отправляем GET-запрос и получаем HTML-код страницы с новостью
    news_soup = BeautifulSoup(news_response.text, 'html.parser')  # Парсим HTML-код страницы с новостью

    # Ищем title, description, keywords, content
    title = news_soup.find('title').text  # Title
    description = ''  # Description
    meta_description = news_soup.find('meta', attrs={'name': 'description'})
    if meta_description:
        description = meta_description['content']

    keywords = ''  # Keywords
    meta_keywords = news_soup.find('meta', attrs={'name': 'keywords'})
    if meta_keywords:
        keywords = meta_keywords['content']

    content = ''  # Content
    article_body = news_soup.find('div', class_='article-body')
    if article_body:
        content = article_body.text
    # Формируем словарь с данными о новости
    news_data = {
        'title': title,
        'description': description,
        'keywords': keywords,
        'content': content
    }
    # Сохраняем данные о новости в файл
    with open('news.json', 'w+') as f:
        json.dump(news_data, f)
        print(f)
    # Публикуем новость на сайте с движком WordPress
    wp = Client('http://example.com/xmlrpc.php', 'username', 'password')  # Авторизуемся на сайте с движком WordPress

    post = WordPressPost()  # Создаем пост
    post.title = title  # Задаем title
    post.content = content  # Задаем content
    post.terms_names = {
        'post_tag': [topic],  # Задаем теги
        'category': ['News']  # Задаем категорию
    }

    post.post_status = 'publish'  # Указываем, что пост должен быть опубликован

    wp.call(NewPost(post))  # Отправляем POST-запрос, чтобы опубликовать пост

    time.sleep(5)  # Задержка в 5 секунд
