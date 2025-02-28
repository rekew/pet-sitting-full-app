from pydantic import BaseModel
from typing import Optional

class NannyCreate(BaseModel):
    location:str
    bio:Optional[str] = None
    offers_grooming:Optional[bool] = False
   

class NannyOut(BaseModel):
    id:int
    location:str
    rating:float 
    bio:Optional[str] = None
    offers_grooming:Optional[bool] = False
    user_name:str

    class Config:
        orm_mode = True