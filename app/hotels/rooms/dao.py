from datetime import date

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.hotels.models import Hotels
from app.database import async_session_maker
from sqlalchemy import select, and_
from app.hotels.rooms.schemas import SRoomsTest


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def test_get_rooms(cls):
        async with async_session_maker() as session:
            query = select(Rooms.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def test_get_rooms_2(cls):
        async with async_session_maker() as session:
            query = select(
                Bookings.__table__.columns,
                Rooms.__table__.columns
            ).join(
                Rooms, Bookings.room_id == Rooms.id, isouter=True
            )
            result = await session.execute(query)
            return result.mappings().all()


#     @classmethod
#     async def get_rooms(cls, hotel_id: int, date_from: date, date_to: date):
#         async with async_session_maker() as session:
#             query = select(Bookings).where(
#                 and_(
#                     Bookings. == hotel_id,
#
#                 )
#
#                 """
#                 WITH t1 AS(
# SELECT *
# FROM bookings
# JOIN rooms ON bookings.room_id = rooms.id
# JOIN hotels ON rooms.hotel_id = hotels.id
# WHERE hotel_id = 1 AND date_from <= '2023-06-24' AND date_to >= '2023-06-20')
# SELECT *
# FROM rooms
# JOIN hotels ON rooms.hotel_id = hotels.id
#                 """
            
