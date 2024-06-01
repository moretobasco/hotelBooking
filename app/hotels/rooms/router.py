from datetime import date
from sqlalchemy import select
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomsTest
from app.bookings.schemas import SBookingRooms
from app.users.models import Users
from app.users.dependencies import get_current_user
from fastapi import Depends

from app.hotels.router import router


@router.get('/{hotel_id}/rooms')
async def get_rooms(date_from: date, date_to: date):
    return await RoomsDAO.get_rooms(date_from, date_to)
