from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database, crud

app = FastAPI()

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(database.get_db)):
    return crud.create_user(db, username, password)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = crud.authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login OK", "username": db_user.username}

@app.get("/auctions/")
def list_auctions(db: Session = Depends(database.get_db)):
    return crud.get_auctions(db)

@app.post("/auctions/")
def create_auction(a: schemas.AuctionCreate, db: Session = Depends(database.get_db)):
    return crud.create_auction(db, a)
