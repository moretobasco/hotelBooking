from datetime import date

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.hotels.models import Hotels
from app.database import async_session_maker
from sqlalchemy import select, and_


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_rooms(cls, hotel_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = select(Bookings).where(
                and_(
                    Bookings. == hotel_id,

                )
            
