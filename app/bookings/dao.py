from sqlalchemy import Select, and_, or_, func, select

from app.bookings.models import Bookings
from app.rooms.models import Rooms
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls, room_id, date_from, date_to):
        booked_rooms = select(Bookings).where(
            and_(
                Bookings.room_id == room_id,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    )
                )
            )
        ).cte('booked_rooms')

        get_rooms_left = select(
            ()
        )
