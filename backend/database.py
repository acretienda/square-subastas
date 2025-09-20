import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Copia aquí la URL interna que Render te da
DATABASE_URL = "postgresql://user_subastas_db:ymB6UlzVr9AouYVN9BUbSOVwKAYfFLBv@dpg-d37ik73uibrs7393iu50-a/subastas_db_9nmw"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
