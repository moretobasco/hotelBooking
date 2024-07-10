from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, VARCHAR


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    bookings: Mapped[list["Bookings"]] = relationship(back_populates='user')

    def __str__(self):
        return f'User {self.email}'
