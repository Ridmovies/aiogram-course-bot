from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select

from app.database import async_session, get_session
from app.users.models import User
from app.users.service import UserService

user_router = Router()

@user_router.message(Command('users'))
async def get_users(message: Message) -> None:
    users = await UserService.get_all()
    await message.answer(f"users: {users}")
