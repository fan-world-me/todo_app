[![Telegram](https://img.shields.io/badge/Telegram-@fan__world__me-2CA5E0?style=flat-square&logo=telegram)](https://t.me/fan_world_me)   [![Discord](https://img.shields.io/badge/Discord-fan__world__me-5865F2?style=flat-square&logo=discord)](https://discord.com/users/1040301536036786248)   [![GitHub](https://img.shields.io/badge/GitHub-fan--world--me-181717?style=flat-square&logo=github)](https://github.com/fan-world-me)   [![Portfolio](https://img.shields.io/badge/Portfolio-fan--world--me.github.io-00e5ff?style=flat-square&logo=githubpages&logoColor=white)](https://fan-world-me.github.io/)

# ✦ Cosmic Todo ✦

> написано за один вечер. да, весь.

Полноценный todo-лист на **FastAPI + SQLAlchemy + SQLite**, с асинхронными запросами, кешированием (Redis, graceful fallback), хешированием паролей (bcrypt), JWT-аутентификацией и glassmorphism-дизайном в стиле Cosmic Cyan.

### 💭 Возможности

- 🔐 **JWT-авторизация** — регистрация и логин, пароли хешируются через bcrypt
- ⚡ **Асинхронные запросы** — SQLAlchemy 2.0 (async) + aiosqlite
- 🧠 **Redis-кеш** — опциональный, без него приложение работает нормально
- 🪟 **Glassmorphism UI** — Vanilla JS + CSS в стиле Cosmic Cyan, шрифт Monocraft
- 📖 **Swagger UI** — документация API на `/docs`

---

### 🧰 Tech Stack

| Слой | Технология |
|---|---|
| Backend | FastAPI, Uvicorn |
| ORM | SQLAlchemy 2.0 (async) |
| DB | SQLite (aiosqlite) |
| Cache | Redis (опционально) |
| Auth | JWT (python-jose) + bcrypt (passlib) |
| Frontend | Vanilla JS + CSS Glassmorphism |
| Font | Monocraft |

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-optional-DC382D?style=flat-square&logo=redis&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-auth-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)

---

### 🗂️ Структура

```
todo_app/
├── main.py          — точка входа, FastAPI app
├── database.py      — движок БД, сессии
├── models.py        — SQLAlchemy модели (User, Todo)
├── schemas.py       — Pydantic схемы
├── auth.py          — JWT + bcrypt
├── cache.py         — Redis-кеш (graceful fallback)
├── routers/
│   ├── auth.py      — /auth/register, /auth/token
│   └── todos.py     — CRUD /todos/
├── templates/
│   └── index.html   — SPA
├── static/
│   └── style.css    — Cosmic Cyan Glassmorphism
├── requirements.txt
├── .env.example
└── .gitignore
```

---

### 🚀 Запуск

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

### 🔌 API

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

### 📄 Лицензия

[GNU General Public License v3.0](LICENSE) © [fan-world-me](https://github.com/fan-world-me)

---

Made with 🩵 in Ukraine 🇺🇦

[![Telegram](https://img.shields.io/badge/Telegram-@fan__world__me-2CA5E0?style=flat-square&logo=telegram)](https://t.me/fan_world_me)   [![Discord](https://img.shields.io/badge/Discord-fan__world__me-5865F2?style=flat-square&logo=discord)](https://discord.com/users/1040301536036786248)   [![Portfolio](https://img.shields.io/badge/Portfolio-fan--world--me.github.io-00e5ff?style=flat-square&logo=githubpages&logoColor=white)](https://fan-world-me.github.io/)
