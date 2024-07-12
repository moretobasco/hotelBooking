from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    page_size = 100
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = 'Пользователь'
    name_plural = 'Пользователи'
    icon = 'fa-solid fa-user'


class BookingsAdmin(ModelView, model=Bookings):
    page_size = 100
    column_list = '__all__'
    name = 'Бронь'
    name_plural = 'Брони'
    icon = 'fa-solid fa-hotel'


class HotelsAdmin(ModelView, model=Hotels):
    page_size = 100
    column_list = '__all__'
    name = 'Отель'
    name_plural = 'Отели'
    icon = 'fa-solid fa-book'


class RoomsAdmin(ModelView, model=Rooms):
    page_size = 100
    column_list = '__all__'
    name = 'Номер'
    name_plural = 'Номеры'
    icon = 'fa-solid fa-bed'
