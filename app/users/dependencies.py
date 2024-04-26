from fastapi import Request, Depends
from app.exceptions import (
    IncorrectTokenFormatException,
    TokenAbsentException,
    TokenExpiredException,
    UserDoesNotExistException
)
from jose import jwt, JWTError, ExpiredSignatureError
from app.config import settings
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserDoesNotExistException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user_id:
        raise UserDoesNotExistException
    return user
