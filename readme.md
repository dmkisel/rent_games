### Описание проекта

**Название проекта**: Сайт по аренде и продаже настольных игр

**Цель проекта**: Создание веб-сайта для аренды и продажи настольных игр, предоставляющего пользователям возможность бронировать игры, делать покупки и управлять своими заказами через удобный интерфейс. Проект также включает интеграцию с Telegram ботом для подтверждения заказов и получения уведомлений.

#### Основные компоненты:

1. **Frontend**:
    - **?????**
    - **Функционал**:
        - Просмотр каталога игр с фильтрацией и поиском
        - Бронирование игр на определенные даты и время
        - Добавление игр в корзину и оформление заказов
        - Редактирование профиля, верификация пользователя, просмотр истории заказов

2. **Backend**:
    - **FastAPI**
    - **Функционал**:
        - Управление пользователями:
          - FastAPI_users
        - Управление играми:
        - Управление бронированиями:
        - Управление заказами:
          - Yookassa
        - Взаимодействие с Telegram ботом для обработки подтверждений заказов
          - aiogram or telebot

3. **Telegram Bot**:
    - **pyTelegramBotAPI**
    - **Функционал**:
        - Информирование о статусе заказа
        - Подтверждение заказа через взаимодействие с FastAPI
        - Информирование о новых продуктах

4. **Email**:
    - **????**
    - **Функционал**:
        - Верификация пользователя
        - Информирование о статусе заказа


