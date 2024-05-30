from datetime import date
from sqlalchemy import select
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomsTest
from app.bookings.schemas import SBookingRooms

from app.hotels.router import router


@router.get('/{hotel_id}/rooms')
async def get_rooms(hotel_id: int, date_from: date, date_to: date):
    pass


@router.get('/test_rooms')
async def get_rooms_test() -> list[SRoomsTest]:
    return await RoomsDAO.test_get_rooms()


@router.get('/test_rooms2')
async def get_rooms_test_2() -> list[SBookingRooms]:
    return await RoomsDAO.test_get_rooms_2()
