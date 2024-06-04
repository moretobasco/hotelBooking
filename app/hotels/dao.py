from datetime import date

from sqlalchemy import select, func, and_

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def get_hotels_by_location_and_time(cls, location: str, date_from: date, date_to: date):
        async with async_session_maker() as session:
            '''
            WITH booked_rooms AS (
            SELECT room_id, COUNT(room_id) as qbookings
            FROM bookings
            WHERE date_from <= '2024-06-04' AND date_to >= '2024-05-30'
            GROUP BY room_id
            )
        
            SELECT
            hotels.*,
            rooms.hotel_id,
            rooms.quantity - COALESCE(booked_rooms.qbookings, 0) rooms_left
            FROM rooms
            LEFT JOIN booked_rooms ON rooms.id = booked_rooms.room_id
            LEFT JOIN hotels ON rooms.hotel_id = hotels.id
            WHERE rooms.quantity - COALESCE(booked_rooms.qbookings, 0) > 0 AND hotels.location LIKE '%Алтай%'
            ORDER BY hotels.id
            
            
            
            WITH t1 AS (
                WITH booked_rooms AS (
                    SELECT room_id, COUNT(room_id) AS qbookings
                    FROM bookings
                    WHERE date_from <= '2024-06-04' AND date_to >= '2024-05-30'
                    GROUP BY room_id
                    )
            SELECT rooms.hotel_id, SUM(rooms.quantity - COALESCE(booked_rooms.qbookings, 0)) rooms_left
            FROM rooms
            LEFT JOIN booked_rooms on booked_rooms.room_id = rooms.id
            GROUP BY rooms.hotel_id
            )
            SELECT *
            FROM hotels
            JOIN t1 on hotels.id = t1.hotel_id
            WHERE t1.rooms_left > 0 AND hotels.location LIKE '%Алтай%'
            ORDER BY hotels.id
            '''

        booked_rooms = select(
            Bookings.room_id,
            (func.count(Bookings.room_id)).label('qbookings')
        ).where(
            and_(
                Bookings.date_from <= date_to,
                Bookings.date_to >= date_from
            )
        ).group_by(Bookings.room_id).cte('booked_rooms')

        t1 = select(
            Rooms.hotel_id,
            func.sum(Rooms.quantity) - func.coalesce(booked_rooms.c.qbookings, 0)
        ).join(
            booked_rooms, Rooms.id == booked_rooms.c.room_id, isouter=True
        ).group_by(
            Rooms.hotel_id
        ).cte('t1')

        query = select(t1)

        # query = select(
        #     Hotels.__table__.columns
        # ).join(
        #     t1, Hotels.id == t1.c.hotel_id
        # ).where(
        #     and_(
        #         t1.c.rooms_left > 0,
        #         Hotels.location.like(f'%{location}%')
        #     )
        # ).order_by(
        #     Hotels.id
        # )


        # booked_rooms = select(
        #     Bookings.room_id,
        #     (func.count(Bookings.room_id)).label('qbookings')
        # ).where(
        #     and_(
        #         Bookings.date_from <= date_to,
        #         Bookings.date_to >= date_from
        #     )
        # ).group_by(Bookings.room_id).cte('booked_rooms')
        #
        # query = select(
        #     Hotels.__table__.columns,
        #     Rooms.hotel_id,
        #     (Rooms.quantity - func.coalesce(booked_rooms.c.qbookings, 0)).label('rooms_left')
        # ).select_from(Rooms).join(
        #     booked_rooms, Rooms.id == booked_rooms.c.room_id, isouter=True
        # ).join(
        #     Hotels, Rooms.hotel_id == Hotels.id, isouter=True
        # ).where(
        #     and_(
        #         Rooms.quantity - func.coalesce(booked_rooms.c.qbookings, 0) > 0,
        #         Hotels.location.like(f'%{location}%')
        #     )
        # ).order_by(Hotels.id)
        result = await session.execute(query)
        return result.mappings().all()
