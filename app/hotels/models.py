from app.database import Base
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship, mapped_column, Mapped


class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[list["Rooms"]] = relationship(back_populates='hotel')
