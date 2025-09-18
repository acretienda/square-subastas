from sqlalchemy.orm import Session
from . import models, schemas


# ===============================
# Usuarios
# ===============================
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ===============================
# Subastas
# ===============================
def get_auctions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Auction).offset(skip).limit(limit).all()


def get_auction(db: Session, auction_id: int):
    return db.query(models.Auction).filter(models.Auction.id == auction_id).first()


def create_auction(db: Session, auction: schemas.AuctionCreate, user_id: int):
    db_auction = models.Auction(**auction.dict(), owner_id=user_id)
    db.add(db_auction)
    db.commit()
    db.refresh(db_auction)
    return db_auction


# ===============================
# Pujas
# ===============================
def create_bid(db: Session, bid: schemas.BidCreate, auction_id: int, bidder_id: int):
    db_bid = models.Bid(**bid.dict(), auction_id=auction_id, bidder_id=bidder_id)
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid


def get_bids_for_auction(db: Session, auction_id: int):
    return db.query(models.Bid).filter(models.Bid.auction_id == auction_id).all()
