from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas, dependecies 

router = APIRouter(prefix="/sitters", tags=["sitters"])

@router.post("", response_model=schemas.SitterOut, status_code=status.HTTP_201_CREATED)
async def create_sitter(
    payload: schemas.SitterCreate,
    session: AsyncSession = Depends(dependecies.get_session),
):
    user = await session.get(models.User, payload.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Related user not found")

    sitter = models.Sitter(**payload.dict())
    user.is_sitter = True
    session.add(sitter)
    await session.commit()
    await session.refresh(sitter)
    return sitter

@router.get("", response_model=List[schemas.SitterOut])
async def list_sitters(
    city: Optional[str] = None,
    session: AsyncSession = Depends(dependecies.get_session),
):
    stmt = select(models.Sitter)                # ← 2
    if city:
        stmt = stmt.where(models.Sitter.city.ilike(f"%{city}%"))
    result = await session.scalars(stmt)
    return list(result)
