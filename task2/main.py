# Дано: список, содержащий URL страниц
# Требуется: Написать функцию, которая получает из Сети код страниц из списка и сохраняет его (код) на диск.

import requests
from bs4 import BeautifulSoup


def get_html(urls):
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        with open(f'document_{urls.index(url)}.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))


get_html(['https://yandex.ru/',
          'https://google.com/'])
