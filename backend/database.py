# backend/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Tomar la URL de la base de datos de Render
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Crear una clase base para los modelos
Base = declarative_base()

# Crear la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función de ayuda para obtener sesiones
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
