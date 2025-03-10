from aiogram import F, html, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.forms import Form
from app.keyboards import (
    get_inline_keyboard,
    get_reply_keyboard,
    main_kb,
    reply_cars_kb, inline_cars_kb
)
from app.middlewares import TestMiddleware

router = Router()
# Для команд
router.message.middleware(TestMiddleware())
# Для всех событий
# router.message.outer_middleware(TestMiddleware())

# @router.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
                         reply_markup=main_kb())


@router.message(Command('help'))
async def get_help(message: Message) -> None:
    await message.answer(f""" помощь по командам бота:
    /hello - Приветствие
    /help - помощь по командам бота
    /get_photo - показать фото
    /get_message - показать информацию о сообщении в консоль
    /reply - показать кнопки Reply
    /inline - показать кнопки Inline
    /cars - показать кнопки Inline с машинами
    /reg - запуск тестовой формы регистрации (состояния)
    """)


@router.message(F.text == "hello")
async def hello(message: Message) -> None:
    await message.answer("Hello to you too!")


@router.message(F.photo)
async def handle_photo(message: Message) -> None:
    await message.answer(f"Nice photo! ID: {message.photo[-1].file_id}")


@router.message(Command("get_photo"))
async def get_photo(message: Message) -> None:
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMRZ8WPR86YzV5U5wG4DnZAwbHFeGsAAnDsMRtVLilK7HE5lwEEtGMBAAMCAAN5AAM2BA",
        caption="Nice photo!",
    )

@router.message(Command("get_message"))
async def get_message(message: Message) -> None:
    for key, value in message.__dict__.items():
        if isinstance(value, dict):
            print({key: value})
        else:
            print(f"{key}: {value}")


# Обработчик команды /reply
@router.message(Command("reply"))
async def show_buttons(message: Message) -> None:
    # TODO Reply-клавиатура не работает в Telegram Web
    # Получаем клавиатуру
    keyboard = get_reply_keyboard()
    # Отправляем сообщение с Reply-клавиатурой
    await message.answer("Выберите кнопку:", reply_markup=keyboard)


@router.message(Command("inline"))
async def show_inline_buttons(message: Message) -> None:
    # Получаем клавиатуру
    keyboard = get_inline_keyboard()
    # Отправляем сообщение с Inline-клавиатурой
    await message.answer("Выберите кнопку:", reply_markup=keyboard)


# Обработчик нажатий на Inline-кнопки
@router.callback_query()
async def handle_inline_buttons(callback: CallbackQuery) -> None:
    # Получаем данные из callback
    button_data = callback.data

    # Отвечаем на нажатие кнопки
    if button_data == "button1":
        await callback.answer("callback.answer")
    elif button_data == "button2":
        await callback.answer("show_alert=True", show_alert=True)
    elif button_data == "button3":
        await callback.message.edit_text("Edited message", reply_markup=await inline_cars_kb())

    # Убираем "часики" (индикатор загрузки) после нажатия
    await callback.answer()


@router.message(Command("cars"))
async def show_inline_cars(message: Message) -> None:
    # Получаем клавиатуру
    keyboard = await inline_cars_kb()
    # Отправляем сообщение с Inline-клавиатурой
    await message.answer("Выберите кнопку:", reply_markup=keyboard)




# @router.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")

