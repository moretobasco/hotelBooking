from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь уже существует'


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверная почта, или пароль'


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный формат токена'


class RoomCanNotBeBooked(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Не осталось свободных номеров'


class NoBookings(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Нет бронирований'


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен отсутствует'


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Срок действия токена истёк'


class UserDoesNotExistException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Пользователь не существует'


class BookingNotFound(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Бронь не найдена'


class NotYourBooking(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Несоответствие пользователя и брони'
