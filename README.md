Yatube API

Социальная сеть для блогеров — бэкенд на Django REST Framework.

ОПИСАНИЕ
Проект предоставляет REST API для публикации постов, комментариев, управления группами и подписками. Реализована аутентификация с помощью JWT-токенов. Документация доступна после запуска по адресу /redoc/.

Основные возможности:
- Создание, чтение, обновление и удаление постов (только автором)
- Комментирование постов (только автором комментария)
- Просмотр групп
- Подписка на других пользователей и получение списка подписок (с поиском)
- JWT-аутентификация (получение, обновление и проверка токенов)

ТЕХНОЛОГИИ
Python 3.10, Django 3.2, Django REST Framework, djangorestframework-simplejwt, SQLite (по умолчанию)

УСТАНОВКА И ЗАПУСК
Клонируйте репозиторий и перейдите в папку проекта:
git clone <URL вашего репозитория>
cd api-final-yatube-ad

Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate      # для Linux/macOS
# или
venv\Scripts\activate         # для Windows

Установите зависимости:
pip install -r requirements.txt

Выполните миграции:
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Теперь документация доступна по адресу: http://127.0.0.1:8000/redoc/

ПРИМЕРЫ ЗАПРОСОВ К API

1. Получение JWT-токена
POST /api/v1/jwt/create/
Тело запроса: {"username": "your_username", "password": "your_password"}
Ответ: {"refresh": "eyJ...", "access": "eyJ..."}

2. Получение списка постов (доступно без авторизации)
GET /api/v1/posts/
Ответ (с пагинацией):
{
  "count": 123,
  "next": "http://.../?offset=100&limit=100",
  "previous": null,
  "results": [
    {"id": 1, "author": "alice", "text": "Привет, мир!", "pub_date": "2026-08-30T10:00:00Z", "image": null, "group": 1}
  ]
}

3. Создание поста (требуется авторизация)
POST /api/v1/posts/
Заголовок: Authorization: Bearer <access_token>
Тело запроса: {"text": "Мой новый пост", "group": 2}
Ответ: {"id": 10, "author": "your_username", "text": "Мой новый пост", "pub_date": "2026-08-30T12:00:00Z", "image": null, "group": 2}

4. Подписка на пользователя (только авторизованные)
POST /api/v1/follow/
Заголовок: Authorization: Bearer <access_token>
Тело запроса: {"following": "bob"}
Ответ: {"user": "your_username", "following": "bob"}

5. Получение списка подписок (с поиском по имени)
GET /api/v1/follow/?search=bob
Заголовок: Authorization: Bearer <access_token>
Ответ: [{"user": "your_username", "following": "bob"}]