from datetime import date

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.hotels.models import Hotels
from app.database import async_session_maker
from sqlalchemy import select, and_, func
from app.hotels.rooms.schemas import SRoomsTest


class RoomsDAO(BaseDAO):
    model = Rooms



    @classmethod
    async def get_rooms(cls, date_from: date, date_to: date):
        async with async_session_maker() as session:
            """
            WITH booked_rooms AS (
                SELECT room_id, COUNT(room_id) as qbookings
                FROM bookings
                WHERE date_from <= '2024-06-04' AND date_to >= '2024-05-30'
                GROUP BY room_id
                )
            SELECT
                *,
                rooms.quantity - booked_rooms.qbookings rooms_left,
                (CAST('2024-06-04' AS date) - cast('2024-05-30' as date)) * price as total_cost
            FROM rooms
            JOIN booked_rooms ON rooms.id = booked_rooms.room_id
            WHERE hotel_id = 2
            """
            booked_rooms = select(
                Bookings.room_id,
                func.count(Bookings.room_id).label('qbookings')).where(
                and_(
                    Bookings.date_from <= date_to,
                    Bookings.date_to >= date_from
                )
            ).group_by(Bookings.room_id).cte('booked_rooms')
            query = select(
                Rooms.__table__.columns,
                (Rooms.quantity - booked_rooms.c.qbookings).label('rooms_left')
            ).join(booked_rooms, booked_rooms.c.room_id == Rooms.id)
            result = await session.execute(query)
            return result.mappings().all()


            
