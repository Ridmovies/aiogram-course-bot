from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()  # Состояние для имени
    age = State()   # Состояние для возраста
    gender = State()  # Состояние для пола