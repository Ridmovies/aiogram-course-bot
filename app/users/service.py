from sqlalchemy import select

from app.database import async_session
from app.services import BaseService
from app.users.models import User


class UserService(BaseService):
    model = User

    @classmethod
    async def create_user(cls, tg_id: int):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if user is None:
                session.add(User(tg_id=tg_id))
                await session.commit()
        
    