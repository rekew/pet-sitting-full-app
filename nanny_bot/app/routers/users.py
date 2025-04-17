from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas, dependecies

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(payload: schemas.UserCreate, session: AsyncSession = Depends(dependecies.get_session)):
    existing = await session.scalar(models.User.select().where(models.User.telegram_id == payload.telegram_id))  # type: ignore[attr-defined]
    if existing:
        raise HTTPException(status_code=400, detail="User already registered")
    user = models.User(**payload.dict())  #
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int, session: AsyncSession = Depends(dependecies.get_session)):
    user = await session.get(models.User, user_id)
    if not user:
       raise HTTPException(status_code=404, detail="User not found")
    return user