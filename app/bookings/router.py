from datetime import date

from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingRooms
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import RoomCanNotBeBooked, NoBookings
from pydantic import parse_obj_as
from app.tasks.tasks import send_booking_confirmation_email

router = APIRouter(prefix='/bookings', tags=['Бронирования'])


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    """ Получение бронирования (без информации номеров) """
    return await BookingDAO.find_all(user_id=user.id)


@router.post('')
async def add_booking(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCanNotBeBooked
    booking_dict = parse_obj_as(SBooking, booking).dict()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return booking_dict


@router.delete('/{booking_id}')
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
    """ Удаление бронирования """
    return await BookingDAO.delete_my_booking(user=user, booking_id=booking_id)


@router.get('/mybookings')
async def get_my_bookings(user: Users = Depends(get_current_user)) -> list[SBookingRooms]:
    """ Получение списка бронирований (с информацией номеров) """
    my_bookings = await BookingDAO.get_my_bookings(user)
    if not my_bookings:
        raise NoBookings
    return my_bookings



