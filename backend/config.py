# config.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a la base de datos de Render (Internal Database URL)
DATABASE_URL = "postgresql://user_subastas_db:ymB6UlzVr9AouYVN9BUbSOVwKAYfFLBv@dpg-d37ik73uibrs7393iu50-a/subastas_db_9nmw"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Configurar sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()


# Dependencia para obtener sesión en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
