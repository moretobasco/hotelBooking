from fastapi import FastAPI, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing_extensions import Annotated
from typing import Union
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms
from app.pages.router import router as router_pages
from app.images.router import router as router_images
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from contextlib import asynccontextmanager
import logging

from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)

app.mount('/static', StaticFiles(directory='app/static'), 'static')

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)

# class HotelsSearchArgs:
#     def __init__(
#             self,
#             location: str,
#             date_from: date,
#             date_to: date,
#             has_parking: Annotated[Union[bool], Query()] = None,
#             has_spa: Union[bool] = None,
#             stars: int = Query(ge=1, le=5, default=None),
#     ):
#         self.location = location,
#         self.date_from = date_from,
#         self.date_to = date_to,
#         self.has_parking = has_parking,
#         self.has_spa = has_spa
#         self.stars = stars
#
#
# class SHotel(BaseModel):
#     address: str
#     name: str
#     stars: int


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
