import json

import pytest
from app.database import Base, async_session_maker, engine
from app.config import settings
from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users


@pytest.fixture(autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with async_session_maker() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f'app/tests/mock_{model}.json', 'r') as file:
            return json.load(file)

    hotels = open_mock_json('hotels')
    bookings = open_mock_json('bookings')
    rooms = open_mock_json('rooms')
    users = open_mock_json('users')
