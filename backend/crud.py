from sqlalchemy.orm import Session
from . import models

def get_auctions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Auction).offset(skip).limit(limit).all()

def create_auction(db: Session, auction: models.Auction):
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return auction
