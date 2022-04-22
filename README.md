# API_FINAL_YATUBE
## Назначение
Проект включает в себя функционал для обмена информацией 
с приложением Yatube через API. Теперь вы можете автоматизировать 
процесс 
выгрузки постов, комментариев, подписок, групп, а также добавлять новые посты, 
комментарии и делать подписки.
## Установка проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/taren4ik/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

##Примеры. Некоторые примеры запросов к API.
1. Добавление поста через эндпоинт api/v1/posts/

```
text - string (required)
image - string or null <binary>
group - integer or null (id сообщества)

{
"text": "string",
"image": "string",
"group": 0
}
```
2. Получение публикации от эндпоинта api/v1/posts/{id}/

```
id - integer (required)

{
"id": 0
}
```
