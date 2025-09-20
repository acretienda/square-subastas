from sqlalchemy import Column, Integer, String, Float, DateTime
from config import Base
from datetime import datetime

class Auction(Base):
    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    starting_price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
