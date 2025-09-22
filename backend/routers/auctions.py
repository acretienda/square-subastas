from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Auction, User
from schemas import AuctionCreate, AuctionOut

router = APIRouter(tags=["auctions"])

@router.post("/auctions/", response_model=AuctionOut)
def create_auction(auction: AuctionCreate, owner_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == owner_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Owner not found")
    new_auction = Auction(
        title=auction.title,
        start_price=auction.start_price,
        current_price=auction.start_price,
        owner_id=owner_id
    )
    db.add(new_auction)
    db.commit()
    db.refresh(new_auction)
    return new_auction

@router.get("/auctions/", response_model=list[AuctionOut])
def list_auctions(db: Session = Depends(get_db)):
    return db.query(Auction).all()
