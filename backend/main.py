from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import Base, engine, get_db
from backend import models

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Square Auctions API")

@app.get("/")
def root():
    return {"message": "API de Subastas funcionando!"}

@app.post("/auctions/")
def create_auction(title: str, description: str, starting_price: float, db: Session = Depends(get_db)):
    auction = models.Auction(title=title, description=description, starting_price=starting_price)
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return auction

@app.get("/auctions/")
def list_auctions(db: Session = Depends(get_db)):
    return db.query(models.Auction).all()