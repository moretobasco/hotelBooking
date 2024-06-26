import asyncio
from datetime import date

from fastapi import APIRouter
from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotels, SHotelsInLoc
from fastapi_cache.decorator import cache

router = APIRouter(prefix='/hotels', tags=['/Отели и номера'])


@router.get('/id/{hotel_id}')
async def get_hotels(hotel_id: int) -> list[SHotels]:
    """ Получение конкретного отеля (опционально, может пригодиться для фронтенда) """
    return await HotelsDAO.find_by_id(hotel_id)


@router.get('/{location}')
@cache(expire=180)
async def get_hotels_by_location_and_time(location: str, date_from: date, date_to: date) -> list[SHotelsInLoc]:
    """ Получение списка отелей """
    await asyncio.sleep(3)
    hotels = await HotelsDAO.get_hotels_by_location_and_time(location, date_from, date_to)
    return hotels
