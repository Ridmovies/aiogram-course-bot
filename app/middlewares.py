from aiogram import BaseMiddleware
from typing import Union, List, Callable, Dict, Any, Awaitable

from aiogram.types import Message, CallbackQuery, TelegramObject


class TestMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ) -> Any:
        print("Действия до обработки сообщения")
        result = await handler(event, data)
        print("Действия после обработки сообщения")
        return result


