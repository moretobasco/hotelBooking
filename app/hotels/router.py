from fastapi import APIRouter
from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotels

router = APIRouter(prefix='/hotels', tags=['/Отели и номера'])


@router.get('/id/{hotel_id}')
async def get_hotels(hotel_id: int) -> list[SHotels]:
    """ Получение конкретного отеля (опционально, может пригодиться для фронтенда) """
    return await HotelsDAO.find_by_id(hotel_id)
