from fastapi import Request, Depends
from app.exceptions import IncorrectEmailOrPasswordException


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise IncorrectEmailOrPasswordException
    return token


def get_current_user(token: str = Depends(get_token)):
    pass
