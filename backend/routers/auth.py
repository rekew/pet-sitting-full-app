from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal,get_db
from models.model import User, Nanny
from schemas.user import UserCreate, Token
from schemas.nanny import NannyCreate, NannyOut
from core.security import hash_password, verify_password, create_access_token, get_current_user
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from typing import List, Optional

router = APIRouter()


@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        name=user.name,
        is_nanny=user.is_nanny,
        phone=user.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    
    if user.is_nanny:
        new_nanny = Nanny(user_id=db_user.id, location="Не указано", bio="", offers_grooming=False)
        db.add(new_nanny)
        db.commit()
        db.refresh(new_nanny)


    access_token = create_access_token(
        data={"sub": db_user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": db_user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/create_or_update", response_model=NannyOut)
def create_or_update_nanny_profile(
    email: str,
    nanny_data: NannyCreate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    
    if not user.is_nanny:
        raise HTTPException(status_code=400, detail="User is not a nanny")


    existing_nanny = db.query(Nanny).filter(Nanny.user_id == user.id).first()

    if existing_nanny:
        
        existing_nanny.location = nanny_data.location
        existing_nanny.bio = nanny_data.bio
        existing_nanny.offers_grooming = nanny_data.offers_grooming
    else:
        
        new_nanny = Nanny(
            user_id=user.id,
            location=nanny_data.location,
            bio=nanny_data.bio,
            offers_grooming=nanny_data.offers_grooming
        )
        db.add(new_nanny)

    db.commit()

    nanny = existing_nanny or new_nanny

   
    return NannyOut(
        id=nanny.id,
        location=nanny.location,
        rating=nanny.rating,
        bio=nanny.bio,
        offers_grooming=nanny.offers_grooming,
        user_name=user.name
    )



@router.get("/search", response_model=List[NannyOut])
def search_nannies(
    location: Optional[str] = None,
    min_rating: Optional[float] = None,
    offers_grooming: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Nanny).join(User).filter(User.is_nanny == True)

    if location:
        query = query.filter(Nanny.location.ilike(f"%{location}%"))
    if min_rating is not None:
        query = query.filter(Nanny.rating >= min_rating)
    if offers_grooming is not None:
        query = query.filter(Nanny.offers_grooming == offers_grooming)

    nannies = query.all()
    results = []

    for nanny in nannies:
        results.append(NannyOut(
            id=nanny.id,
            location=nanny.location,
            rating=nanny.rating,
            bio=nanny.bio,
            offers_grooming=nanny.offers_grooming,
            user_name=nanny.user.name
        ))

    return results
