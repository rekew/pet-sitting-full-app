from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[Optional[str]] = mapped_column(String(255), unique=True, nullable=True)
    is_sitter: Mapped[bool] = mapped_column(Boolean, default=False)

    sitter_profile: Mapped["Sitter"] = relationship(back_populates="user", uselist=False)
    pets: Mapped[List["Pet"]] = relationship(back_populates="owner")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="owner")

class Sitter(Base):
    __tablename__ = "sitters"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    bio: Mapped[Optional[str]] = mapped_column(Text)
    city: Mapped[str] = mapped_column(String(100))
    daily_rate: Mapped[int] = mapped_column(Integer)  # in KZT

    user: Mapped[User] = relationship(back_populates="sitter_profile")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="sitter")

class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(100))
    species: Mapped[str] = mapped_column(String(50))
    notes: Mapped[Optional[str]] = mapped_column(Text)

    owner: Mapped[User] = relationship(back_populates="pets")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="pet")

class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    sitter_id: Mapped[int] = mapped_column(ForeignKey("sitters.id", ondelete="CASCADE"))
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id", ondelete="CASCADE"))
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20), default="pending")

    owner: Mapped[User] = relationship(back_populates="bookings")
    sitter: Mapped[Sitter] = relationship(back_populates="bookings")
    pet: Mapped[Pet] = relationship(back_populates="bookings")