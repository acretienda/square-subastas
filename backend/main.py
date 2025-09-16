from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import models, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Square Auctions API")

@app.get('/')
def read_root():
    return {'message': 'API de subastas funcionando'}

@app.get('/auctions')
def list_auctions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_auctions(db, skip=skip, limit=limit)

@app.post('/auctions')
def create_auction(title: str, description: str, starting_price: float, db: Session = Depends(get_db)):
    auction = models.Auction(title=title, description=description, starting_price=starting_price)
    return crud.create_auction(db, auction)
