from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class AuctionCreate(BaseModel):
    title: str
    start_price: float

class AuctionOut(BaseModel):
    id: int
    title: str
    start_price: float
    current_price: float
    owner_id: int
    class Config:
        orm_mode = True
