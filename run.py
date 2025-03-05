import asyncio
import logging
import sys
from os import getenv

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.token import TokenValidationError
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers import router
from app.dev_handlers import dev_router
from app.users.handlers import user_router
from app.states import reg_router

# Загружаем переменные окружения из файла .env
load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN: str = getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Токен не найден в переменных окружения!")

# Для хранения состояний можно использовать MemoryStorage (в памяти)
# storage = MemoryStorage()

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


async def main() -> None:
    # Добавляем роутеры
    dp.include_router(router)
    dp.include_router(dev_router)
    dp.include_router(user_router)
    dp.include_router(reg_router)
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    try:
        await dp.start_polling(bot)
    except TokenValidationError as e:
        print(f"Ошибка валидации токена: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())