from fastapi import APIRouter
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.dao import HotelsDAO
from sqlalchemy import select


router = APIRouter(prefix='/hotels', tags=['/Отели и номера'])


@router.get('/id/{id}')
async def get_hotels(hotel_id: int):
    return await HotelsDAO.find_by_id(hotel_id)
