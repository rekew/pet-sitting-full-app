from core.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_nanny = Column(Boolean, default=False)
    name = Column(String)
    phone = Column(String, nullable=True)

    
    nanny = relationship("Nanny", back_populates="user", uselist=False)

class Nanny(Base):
    __tablename__ = "nannies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Float, default=0.0)
    location = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    offers_grooming=Column(Boolean,default=False)

    
    user = relationship("User", back_populates="nanny")



