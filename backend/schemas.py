from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ===============================
# Usuarios
# ===============================
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ===============================
# Subastas
# ===============================
class AuctionBase(BaseModel):
    title: str
    description: Optional[str] = None
    starting_price: float


class AuctionCreate(AuctionBase):
    pass


class AuctionResponse(AuctionBase):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True


# ===============================
# Pujas
# ===============================
class BidBase(BaseModel):
    amount: float


class BidCreate(BidBase):
    pass


class BidResponse(BidBase):
    id: int
    auction_id: int
    bidder_id: int
    created_at: datetime

    class Config:
        from_attributes = True
