from app.database import async_session_maker
from sqlalchemy import Select
from app.bookings.models import Bookings

class BaseDAO:
    model = None
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = Select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()