from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class AuctionCreate(BaseModel):
    title: str
    starting_price: float
