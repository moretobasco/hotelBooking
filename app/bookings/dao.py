from sqlalchemy import select, and_, or_, func, insert, delete

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms
from app.dao.base import BaseDAO
from app.users.models import Users
from app.exceptions import BookingNotFound, NotYourBooking


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, user_id, room_id, date_from, date_to):
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    Bookings.date_from <= date_to,
                    Bookings.date_to >= date_from
                )
            ).cte('booked_rooms')

            get_rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
            ).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
            ).where(Rooms.id == room_id).group_by(
                Rooms.quantity, booked_rooms.c.room_id
            )

            rooms_left = await session.execute(get_rooms_left)
            rooms_left = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price = price.scalar()
                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                ).returning(Bookings)

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()

            else:
                return None

    @classmethod
    async def get_my_bookings(cls, user: Users):
        async with async_session_maker() as session:
            query = select(
                Bookings.__table__.columns,
                Rooms.__table__.columns
            ).join(
                Rooms, Bookings.room_id == Rooms.id, isouter=True
            ).where(Bookings.user_id == user.id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def delete_my_booking(cls, user: Users, booking_id: int):
        async with async_session_maker() as session:
            booking = select(Bookings.user_id).where(Bookings.id == booking_id)
            booking = await session.execute(booking)
            booking = booking.scalar()
            if not booking:
                raise BookingNotFound
            if booking == user.id:
                delete_booking = delete(Bookings).where(Bookings.id == booking_id)
                await session.execute(delete_booking)
                await session.commit()
            else:
                return NotYourBooking
