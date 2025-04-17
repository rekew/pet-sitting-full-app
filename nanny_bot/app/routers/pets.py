from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas, dependencies

router = APIRouter(prefix="/pets", tags=["pets"])

@router.post("", response_model=schemas.PetOut, status_code=status.HTTP_201_CREATED)
async def create_pet(payload: schemas.PetCreate, session: AsyncSession = Depends(dependencies.get_session)):
    owner = await session.get(models.User, payload.owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    pet = models.Pet(**payload.dict())  
    session.add(pet)
    await session.commit()
    await session.refresh(pet)
    return pet