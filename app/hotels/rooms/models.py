from app.database import Base
from app.hotels.models import Hotels
from app.bookings.models import Bookings
from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional


class Rooms(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[list[str]] = mapped_column(JSON)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped["Hotels"] = relationship(back_populates='rooms')
    bookings: Mapped[list["Bookings"]] = relationship(back_populates='room')

    def __str__(self):
        return {self.name}
