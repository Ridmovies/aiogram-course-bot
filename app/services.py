from sqlalchemy import select

from app.database import async_session


class BaseService:
    model = None

    @classmethod
    async def get_all(cls, order_by=None, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            # if order_by:
            if order_by is not None:
                query = query.order_by(order_by)
            result = await session.execute(query)
            return result.scalars().all()

    # @classmethod
    # async def create(cls, session: AsyncSession, data, user_id: int = None):
    #     data_dict = data.model_dump()
    #     if user_id is not None:
    #         instance = cls.model(**data_dict, user_id=user_id)
    #     else:
    #         instance = cls.model(**data_dict)
    #     session.add(instance)
    #     await session.commit()
    #     return instance