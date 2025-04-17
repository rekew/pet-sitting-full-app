from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas, dependencies

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.post("", response_model=schemas.BookingOut, status_code=status.HTTP_201_CREATED)
async def create_booking(payload: schemas.BookingCreate, session: AsyncSession = Depends(dependencies.get_session)):
    owner = await session.get(models.User, payload.owner_id)
    sitter = await session.get(models.Sitter, payload.sitter_id)
    pet = await session.get(models.Pet, payload.pet_id)
    if not all([owner, sitter, pet]):
        raise HTTPException(status_code=404, detail="Owner, sitter, or pet not found")
    booking = models.Booking(**payload.dict(), status="pending")  
    session.add(booking)
    await session.commit()
    await session.refresh(booking)
    return booking

@router.get("/{booking_id}", response_model=schemas.BookingOut)
async def get_booking(booking_id: int, session: AsyncSession = Depends(dependencies.get_session)):
    booking = await session.get(models.Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking