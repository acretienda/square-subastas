from sqlalchemy.orm import Session
from . import models, schemas

def get_auctions(db: Session):
    return db.query(models.Auction).all()

def create_auction(db: Session, auction: schemas.AuctionCreate):
    db_auction = models.Auction(**auction.dict())
    db.add(db_auction)
    db.commit()
    db.refresh(db_auction)
    return db_auction
