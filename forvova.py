import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import sqlite3
import shutil

url = 'https://lifehacker.ru/topics/sport/'

urlheader = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Accept-language': 'ru-RU,ru;q=0.9'
}
media_folder = 'media'
if not os.path.exists(media_folder):
    os.makedirs(media_folder)

session = requests.Session()

def tup(func):
    def wrapper(*args, **kwargs):
        c = func()
        for car in c:
            lin = car.find('img')['srcset']
            # lim = lin.endswith('1280x640.jpg')
            print(lin)
    return wrapper

@tup
def get_card_image(link):
    result_card = session.get(url=link, headers=urlheader)
    beautifulsoup_card: BeautifulSoup = BeautifulSoup(markup=result_card.content, features='lxml')
    images = beautifulsoup_card.find_all(name='img')
    print(images)


def get_card_content(link):
    try:
        result_card = session.get(url=link, headers=urlheader)
        result_card.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при получении карточки: {e}')
    else:
        beautifulsoup_card: BeautifulSoup = BeautifulSoup(markup=result_card.content, features='lxml')
        title = beautifulsoup_card.find(name='h1', attrs={'class': 'article-card__title'}).text
        article = beautifulsoup_card.find(name='article').text
        images = beautifulsoup_card.find_all(name='img')
        # for car in images:
        #     lin = car.find('img')['srcset']
        #     # lim = lin.endswith('1280x640.jpg')

        conn = sqlite3.connect('articles.db')
        c = conn.cursor()
        c.execute("INSERT INTO articles (title, link, content) VALUES (?, ?, ?)", (title,  link, article))

        conn.commit()
        conn.close()




try:
    response_page = session.get(url=url, headers=urlheader)
    response_page.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'Ошибка при получении страницы: {e}')
else:
    beautifulsoup: BeautifulSoup = BeautifulSoup(markup=response_page.content, features='lxml')
    cards = beautifulsoup.find_all(name='div', class_='article-card__small-wrapper')
    num_cards = len(cards)
    print(f'Количество карточек:  {num_cards}')

    links = []
    for card in cards:
        link = card.find('a')['href']
        link = urljoin(base=url, url=link)
        links.append(link)

    # for car in images:
    #     lin = i.find('img')['srcset']
    #     lim = lin.endswith('1280x640.jpg')
    #     print(lin)
        # l.append(lin)

    #
    # for card in cards:
    #     link = card.find('a')['href']
    #     link = urljoin(base=url, url=link)
    #     links.append(link)

    # for image in images:
    #     image_url = image['src']
    #     image_name = os.path.basename(image_url)
    #     image_path = os.path.join(media_folder, image_name)
    #     response = session.get(image_url, stream=True)
    #     with open(image_path, 'wb') as f:
    #         shutil.copyfileobj(response.raw, f)

    with ThreadPoolExecutor() as executor:
        executor.map(get_card_content, links)
        executor.map(get_card_image, links)


conn = sqlite3.connect('articles.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, link TEXT, content TEXT, images BLOB)")
conn.commit()
conn.close()


def printdbtable():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute("SELECT * FROM articles")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

printdbtable()