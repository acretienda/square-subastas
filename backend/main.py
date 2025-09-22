from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, User, Auction, Bid, get_db, engine
from auth import get_current_user, create_access_token, authenticate_user, get_password_hash
from pydantic import BaseModel
from datetime import datetime

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# -------- Esquemas Pydantic --------
class UserCreate(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AuctionCreate(BaseModel):
    title: str
    description: str
    start_price: float

class BidCreate(BaseModel):
    amount: float

# -------- Rutas --------
@app.get("/")
def root():
    return {"message": "API de Subastas funcionando 🎉"}

@app.post("/register/", response_model=TokenResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    hashed_pw = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token = create_access_token(data={"sub": new_user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/login/", response_model=TokenResponse)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/auctions/")
def create_auction(auction: AuctionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_auction = Auction(
        title=auction.title,
        description=auction.description,
        start_price=auction.start_price,
        owner_id=current_user.id
    )
    db.add(new_auction)
    db.commit()
    db.refresh(new_auction)
    return {"msg": "Subasta creada", "auction_id": new_auction.id}

@app.get("/auctions/")
def list_auctions(db: Session = Depends(get_db)):
    return db.query(Auction).all()

@app.post("/auctions/{auction_id}/bid/")
def place_bid(auction_id: int, bid: BidCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    auction = db.query(Auction).filter(Auction.id == auction_id).first()
    if not auction:
        raise HTTPException(status_code=404, detail="Subasta no encontrada")
    new_bid = Bid(
        amount=bid.amount,
        user_id=current_user.id,
        auction_id=auction.id,
        timestamp=datetime.utcnow()
    )
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    return {"msg": "Puja realizada", "bid_id": new_bid.id}
