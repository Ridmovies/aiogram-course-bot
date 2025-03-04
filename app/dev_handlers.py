from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from app.database import create_tables, async_session
from app.users.models import User

dev_router = Router()


@dev_router.message(Command('dev'))
async def get_dev(message: Message) -> None:
    await message.answer("Dev!!!")


@dev_router.message(Command('create_db'))
async def create_database(message: Message) -> None:
    await create_tables()
    await message.answer("Create tables!!!")

