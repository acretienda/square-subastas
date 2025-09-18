from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ⚡ Coge la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://subastas_db_user:fJc1OootrjKeyIHxaIsj6ps0DUnjhY9r@dpg-d33j79idbo4c73b97s1g-a:5432/subastas_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 👉 Dependencia para usar en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
