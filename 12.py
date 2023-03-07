import json
news_data = 'xuy'
with open('news.json', 'w') as f:
    json.dump(news_data, f)
    print(f)
# Публикуем новость на сайте с движком WordPress
# wp = Client('http://example.com/xmlrpc.php', 'username', 'password')  # Авторизуемся на сайте с движком WordPress
#
# post = WordPressPost()  # Создаем пост
# post.title = title  # Задаем title
# post.content = content  # Задаем content
# post.terms_names = {
#     'post_tag': [topic],  # Задаем теги
#     'category': ['News']  # Задаем категорию
# }