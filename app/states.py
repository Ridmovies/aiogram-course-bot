from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.forms import Form

reg_router = Router()


################# State handlers #################

# Регистрация сообщений
@reg_router.message(Command("reg"))
async def reg_form(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("Как вас зовут?")

@reg_router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await state.set_state(Form.age)
    await message.reply("Сколько вам лет?")

@reg_router.message(Form.age)
async def process_age(message: Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await state.set_state(Form.gender)
    await message.reply("Какой у вас пол?")

@reg_router.message(Form.gender)
async def process_gender(message: Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    data = await state.get_data()
    await message.answer(f"{data['name']}, {data['age']} лет, пол: {data['gender']} \nИнформация успешно сохранена!")
    await state.clear()