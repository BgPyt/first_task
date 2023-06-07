# Установка и запуск
<ol>
  <li>Клонировать этот репозиторий <code>git clone https://github.com/BgPyt/first_task.git</code></li>
  <li>В env файле где <strong>PG_ADMIN_EMAI</strong> и <strong>PG_ADMIN_PASSWORD</strong> вставить свои значения для входа в БД-интерфейс</strong></li>
  <li>Создание образов и запуск контейнеров в фоновом режиме<code>docker-compose up -d</code></li>
</ol>
<blockquote>Доступ к документаци к тестовому API http://localhost:8000/docs</blockquote>

#  Реализация 
<ul>Стек применения:
  <li>Fastapi</li>
  <li>alembic</li>
  <li>асинхроннй движок - <b>asyncpg2</b></li>
  <li>Sqlalchemy</li>
  <li>Pydantic</li>
  <li>aiohttp</li>
  <li>Postgresql</li>
</ul>

POST-запрос вида:
<br>
URL: http://localhost:8000/question
<br>
Request body (raw - JSON): {question_num: int}
<br>
Response: Option[Quiz]
<br>
<blockquote>После удаления контейнеров содержимое бд сохраняется в томе</blockquote>
