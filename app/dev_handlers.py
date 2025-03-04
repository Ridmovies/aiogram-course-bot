from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

dev_router = Router()


@dev_router.message(Command('dev'))
async def get_dev(message: Message) -> None:
    await message.answer("Dev!!!")