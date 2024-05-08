from fastapi import APIRouter

router = APIRouter(prefix='/hotels', tags=['/Отели и номера'])


@router.get('/{hotel_id}/rooms')
async def get_hotels():
    pass
