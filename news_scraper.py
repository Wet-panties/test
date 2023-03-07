import requests
from bs4 import BeautifulSoup
import re
import json
import time
import urllib.request
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

# Задаем тематику для поиска новостей
topic = 'News'
print(topic, ' 1')
# Формируем ссылку для поиска новостей
url = 'https://www.google.com/search?q=' + topic + '&source=lnms&tbm=nws'
print(url, ' 2')
# Отправляем GET-запрос и получаем HTML-код страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(response, ' 3')
print(soup, ' 4')

# Ищем в HTML-коде ссылки на новости
news_links = soup.find_all('a', class_='lLrAF')
print(news_links, ' 5')

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
    with open('news.json', 'w') as f:
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

