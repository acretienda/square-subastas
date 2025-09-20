from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL interna de Render (la que me diste)
DATABASE_URL = "postgresql://user_subastas_db:ymB6UlzVr9AouYVN9BUbSOVwKAYfFLBv@dpg-d37ik73uibrs7393iu50-a/subastas_db_9nmw"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
