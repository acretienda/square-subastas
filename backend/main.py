from fastapi import FastAPI
from database import engine, Base
import models

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🚀 Bienvenido a la API de Subastas con Render y PostgreSQL"}

@app.get("/health")
def health():
    return {"status": "ok"}
