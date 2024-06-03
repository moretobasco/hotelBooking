from fastapi import FastAPI, Query, Depends
from typing_extensions import Annotated
from typing import Union
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.pages.router import router as router_pages

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_pages)


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_parking: Annotated[Union[bool], Query()] = None,
            has_spa: Union[bool] = None,
            stars: int = Query(ge=1, le=5, default=None),
    ):
        self.location = location,
        self.date_from = date_from,
        self.date_to = date_to,
        self.has_parking = has_parking,
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


# @app.get('/hotels', response_model=list[SHotel])
# def get_hotels(
#         search_args: HotelsSearchArgs = Depends()
# ):
#     hotels = [
#         {
#             'address': 'ул. Гагарина, 1, Алтай',
#             'name': 'Super Hotel',
#             'stars': 5,
#         }
#     ]
#     return hotels


