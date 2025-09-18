from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Crear las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Subastas con PostgreSQL 🚀"}

# Endpoint para insertar datos demo
@app.post("/seed")
def seed(db: Session = Depends(get_db)):
    demo_products = [
        models.Product(name="Caja de Manzanas", description="Caja de 5kg de manzanas frescas", price=10.00, stock=5),
        models.Product(name="Pan del día", description="Panadería fresco al cierre", price=2.50, stock=20),
        models.Product(name="Bandeja de Croissants", description="Croissants recién hechos (12 uds.)", price=8.00, stock=3),
    ]
    db.add_all(demo_products)
    db.commit()
    return {"message": "Productos demo insertados ✅"}
