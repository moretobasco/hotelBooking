from fastapi import APIRouter

router = APIRouter(prefix='/hotels', tags=['/Отели и номера'])


@router.get('')
async def get_hotels():
    pass
