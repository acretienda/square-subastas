# init_db.py

from config import Base, engine
from models import *

def init_db():
    """
    Crea todas las tablas en la base de datos si no existen.
    """
    print("🔄 Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente.")

if __name__ == "__main__":
    init_db()
