from pydantic  import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    name:str
    is_nanny:bool=False
    phone: Optional[str] = None


class Token(BaseModel):
    access_token:str
    token_type:str