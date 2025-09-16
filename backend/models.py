from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Auction(Base):
    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    starting_price = Column(Float)
    is_active = Column(Boolean, default=True)
