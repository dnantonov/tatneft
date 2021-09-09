В терминале следующей командой клонируем репозиторий:  

`git clone https://github.com/dnantonov/tatneft/ && cd tatneft`

Установка необходимых пакетов:  

`pip install -r requirements.txt`

### Task 1
Первое задание находится в директории task1. Для запуска необходимо ввести команду:  

`python task1/main.py`

### Task 2
Второе задание находится в директории task2. Для запуска программы нужно ввести следующую команду:

`python task2/main.py`

Скрипт сохранит код страниц в папку с программой.

### Task 3
Третье задание находится в директории task3. Для запуска программы нужно ввести следующие команды:
В данном задании использовались следующие библиотеки: Django, Django Rest Framework

`python task3/manage.py makemigrations`

`python task3/manage.py migrate`

`python task3/manage.py runserver`

Данные получаются в формате JSON на странице: http://127.0.0.1:8000/api/
