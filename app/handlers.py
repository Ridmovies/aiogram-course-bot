from aiogram import F, html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command('help'))
async def get_help(message: Message) -> None:
    await message.answer("Help")


@router.message(F.text == "Hello")
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


@router.message(Command("reply"))
async def reply(message: Message) -> None:
    await message.reply("Reply message")


@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")