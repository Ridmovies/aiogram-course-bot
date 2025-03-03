# Telegram Bot на aiogram

Этот репозиторий содержит исходный код телеграм бота, написанного с использованием библиотеки [aiogram](https://docs.aiogram.dev/en/latest/). Бот предназначен для выполнения различных задач, таких как обработка сообщений, команд и callback-запросов.


## Регистрация бота через BotFather

BotFather — это официальный бот от Telegram, который позволяет создавать и управлять ботами.

1. Откройте Telegram и найдите бота **BotFather** (можно найти через поиск по имени `@BotFather`).
2. Запустите BotFather и отправьте команду `/start`.
3. Для создания нового бота отправьте команду `/newbot`.
4. BotFather попросит вас указать имя бота (это имя, которое будет отображаться в списке контактов). Например, `MyTestBot`.
5. Затем нужно указать username бота. Он должен заканчиваться на `bot` (например, `MyTestBot_bot`). Username должен быть уникальным.
6. После успешного создания бота BotFather предоставит вам **токен доступа** (например, `123456789:ABCdefGhIJKlmNoPQRstuVWXyz`). Этот токен необходим для взаимодействия с Telegram API.

---

## 2. Настройка окружения

После получения токена, его нужно сохранить в безопасном месте. Обычно токен добавляют в переменные окружения или в файл `.env`.

1. Создайте файл `.env` в корневой директории вашего проекта.
2. Добавьте туда токен в следующем формате:
   ```plaintext
   BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRstuVWXyz
   ```
   
## 3. Проверка работы

Убедитесь, что файл .env находится в корневой директории проекта.

Запустите скрипт:
```bash
    python bot.py
```