# ✦ Cosmic Todo ✦

> написано за один вечер. да, весь.

Полноценный todo-лист на **FastAPI + SQLAlchemy + SQLite**, с асинхронными запросами, кешированием (Redis, graceful fallback), хешированием паролей (bcrypt), JWT-аутентификацией и glassmorphism-дизайном в стиле Cosmic Cyan.

---

## Stack

| Слой | Технология |
|---|---|
| Backend | FastAPI, Uvicorn |
| ORM | SQLAlchemy 2.0 (async) |
| DB | SQLite (aiosqlite) |
| Cache | Redis (опционально) |
| Auth | JWT (python-jose) + bcrypt (passlib) |
| Frontend | Vanilla JS + CSS Glassmorphism |
| Font | Monocraft |

---

## Запуск

```bash
# 1. Создать и активировать venv
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Скопировать .env
copy .env.example .env

# 4. Запустить
uvicorn main:app --reload
```

Открыть браузер: http://localhost:8000

> Redis не обязателен — без него кеш просто не работает, приложение работает нормально.

---

## Структура

```
todo_app/
├── main.py          # точка входа, FastAPI app
├── database.py      # движок БД, сессии
├── models.py        # SQLAlchemy модели (User, Todo)
├── schemas.py       # Pydantic схемы
├── auth.py          # JWT + bcrypt
├── cache.py         # Redis-кеш (graceful fallback)
├── routers/
│   ├── auth.py      # /auth/register, /auth/token
│   └── todos.py     # CRUD /todos/
├── templates/
│   └── index.html   # SPA
├── static/
│   └── style.css    # Cosmic Cyan Glassmorphism
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## API

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/auth/register` | — | Регистрация |
| POST | `/auth/token` | — | Логин, получить JWT |
| GET | `/todos/` | ✓ | Список задач |
| POST | `/todos/` | ✓ | Создать задачу |
| PATCH | `/todos/{id}` | ✓ | Обновить задачу |
| DELETE | `/todos/{id}` | ✓ | Удалить задачу |

Swagger UI: http://localhost:8000/docs

---

## License

[GNU General Public License v3.0](LICENSE)
