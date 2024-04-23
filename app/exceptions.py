from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверная почта, или пароль'


class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный формат токена'


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен отсутствует'


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Срок действия токена истёк'


class UserDoesNotExistException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Пользователь не существует'

