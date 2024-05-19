from datetime import date

from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.hotels.models import Hotels
from app.database import async_session_maker


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_rooms(cls, hotel_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            pass
