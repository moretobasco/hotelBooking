from datetime import date
from sqlalchemy import select
from app.hotels.models import Hotels

from app.hotels.router import router


@router.get('/{hotel_id}/rooms')
async def get_rooms(hotel_id: int, date_from: date, date_to: date):
    query = select(Hotels).where(Hotels.id == hotel_id)

