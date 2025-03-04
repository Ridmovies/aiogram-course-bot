from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


# Создаем Reply-клавиатуру с тремя кнопками
def get_reply_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Кнопка 1")],
            [KeyboardButton(text="Кнопка 2")],
            [KeyboardButton(text="Кнопка 3")],
        ],
        resize_keyboard=True,  # Автоматическое изменение размера клавиатуры
        one_time_keyboard=True,  # Скрыть клавиатуру после нажатия (опционально)
    )
    return keyboard


# Создаем Inline-клавиатуру с тремя кнопками
def get_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Кнопка 1", callback_data="button1")],
            [InlineKeyboardButton(text="Кнопка 2", callback_data="button2")],
            [InlineKeyboardButton(text="Кнопка 3", callback_data="button3")],
            [InlineKeyboardButton(text="https://example.com", url="https://example.com")],
        ]
    )
    return keyboard


def main_kb():
    kb_list = [
        [KeyboardButton(text="📖 О нас"), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="📝 Заполнить анкету"), KeyboardButton(text="📚 Каталог")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


cars = ["BMW", "Mercedes", "Audi", "Lexus"]

async def reply_cars_kb():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.button(text=car)
    keyboard.adjust(2, 2)
    return keyboard.as_markup()


async def inline_cars_kb():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.button(text=car, url=f"https://www.google.com/search?q={car}")
    keyboard.adjust(2, 2)
    return keyboard.as_markup()