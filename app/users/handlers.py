from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.users.service import UserService

user_router = Router()

@user_router.message(Command('users'))
async def get_users(message: Message) -> None:
    users = await UserService.get_all()
    users_list = [user.tg_id for user in users]
    await message.answer(f"users: {users_list}")


@user_router.message(Command('create_user'))
async def create_user(message: Message) -> None:
    tg_id: int = message.from_user.id
    user = await UserService.create_user(tg_id)
    await message.answer(f"User created")

