from pydantic import BaseModel

class AuctionBase(BaseModel):
    title: str
    description: str
    starting_price: float

class AuctionCreate(AuctionBase):
    pass

class Auction(AuctionBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
