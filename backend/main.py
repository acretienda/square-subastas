from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config import Base, engine, SessionLocal
import models

# Crear las tablas automáticamente al arrancar
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "🚀 Bienvenido a la API de Subastas"}

@app.post("/auctions/")
def create_auction(title: str, description: str, starting_price: float, db: Session = Depends(get_db)):
    auction = models.Auction(
        title=title,
        description=description,
        starting_price=starting_price
    )
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return auction

@app.get("/auctions/")
def list_auctions(db: Session = Depends(get_db)):
    return db.query(models.Auction).all()
