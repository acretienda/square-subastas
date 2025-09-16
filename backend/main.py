from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

# Crear tablas automáticamente si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Subastas API")

@app.get("/auctions", response_model=list[schemas.Auction])
def read_auctions(db: Session = Depends(get_db)):
    return crud.get_auctions(db)

@app.post("/auctions", response_model=schemas.Auction)
def create_auction(auction: schemas.AuctionCreate, db: Session = Depends(get_db)):
    return crud.create_auction(db, auction)
