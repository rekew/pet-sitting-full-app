from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.model import User
from schemas.user import UserCreate, Token

from core.security import hash_password,verify_password,create_access_token
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES

router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register",response_model=Token)
def register(user:UserCreate,db:Session=Depends(get_db)):
 existing_user = db.query(User).filter(User.email == user.email).first()
 if existing_user:
     raise HTTPException(status_code=400,detail="Email already registered")
 
 hashed_pw=hash_password(user.password)
 db_user=User(email=user.email,hashed_password=hashed_pw,name=user.name,is_nanny=user.is_nanny,phone=user.phone)
 db.add(db_user)
 db.commit()
 db.refresh(db_user)

 access_token = create_access_token(data={"sub": db_user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
 return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login",response_model=Token)
def login_user(user:UserCreate,db:Session=Depends(get_db)):
 db_user=db.query(User).filter(User.email==user.email).first()
 if not db_user or not verify_password(user.password,db_user.hashed_password):
     raise HTTPException(status_code=400,detail="Invalid credentials")
 
 access_token=create_access_token(data={"sub":db_user.email},expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
 return {"access_token":access_token,"token_type":"bearer"}