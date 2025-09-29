from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Auction(Base):
    __tablename__ = "auctions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    starting_price = Column(Float, nullable=False)
    current_price = Column(Float, nullable=True)
