from fastapi import FastAPI
from database import SessionLocal, engine, Base
from models import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend desplegado correctamente"}