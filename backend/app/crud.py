from sqlalchemy.orm import Session
from . import models
from passlib.hash import bcrypt

def create_user(db: Session, username: str, password: str):
    hashed = bcrypt.hash(password)
    user = models.User(username=username, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "username": user.username}

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user: return None
    if not bcrypt.verify(password, user.password_hash): return None
    return user

def get_auctions(db: Session):
    return db.query(models.Auction).all()

def create_auction(db: Session, a):
    auction = models.Auction(title=a.title, starting_price=a.starting_price, current_price=a.starting_price)
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return auction
