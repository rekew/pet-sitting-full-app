from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    telegram_id: int
    name: str = Field(..., max_length=100)
    email: Optional[EmailStr] = None
    is_sitter: bool = False

class UserOut(BaseModel):
    id: int
    telegram_id: int
    name: str
    email: Optional[EmailStr]
    is_sitter: bool

    class Config:
        orm_mode = True

class SitterCreate(BaseModel):
    user_id: int
    bio: Optional[str] = None
    city: str
    daily_rate: int = Field(..., gt=0)

class SitterOut(BaseModel):
    id: int
    user: UserOut
    bio: Optional[str]
    city: str
    daily_rate: int

    class Config:
        orm_mode = True

class PetCreate(BaseModel):
    owner_id: int
    name: str
    species: str
    notes: Optional[str] = None

class PetOut(BaseModel):
    id: int
    owner_id: int
    name: str
    species: str
    notes: Optional[str]

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    owner_id: int
    sitter_id: int
    pet_id: int
    start_date: datetime
    end_date: datetime

class BookingOut(BaseModel):
    id: int
    owner: UserOut
    sitter: SitterOut
    pet: PetOut
    start_date: datetime
    end_date: datetime
    status: str

    class Config:
        orm_mode = True