from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# ============================================================
# Configuración general
# ============================================================

DATABASE_URL = "postgresql://user_subastas_db:ymB6UlzVr9AouYVN9BUbSOVwKAYfFLBv@dpg-d37ik73uibrs7393iu50-a/subastas_db_9nmw"

SECRET_KEY = "supersecreto"   # ⚠️ cámbialo en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# DB
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Seguridad
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# ============================================================
# Modelos
# ============================================================

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password_hash = Column(String(255))
    auctions = relationship("Auction", back_populates="owner")

class Auction(Base):
    __tablename__ = "auctions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    starting_price = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="auctions")

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# ============================================================
# Utilidades
# ============================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def hash_password(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user

# ============================================================
# App FastAPI
# ============================================================

app = FastAPI(title="API Subastas")

@app.get("/")
def root():
    return {"message": "🚀 API de Subastas lista en Render"}

# ---------- Registro ----------
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    user = User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": f"Usuario {username} creado"}

# ---------- Login ----------
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# ---------- Crear subasta ----------
@app.post("/auctions/")
def create_auction(title: str, starting_price: float, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    auction = Auction(title=title, starting_price=starting_price, owner_id=current_user.id)
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return {"message": "Subasta creada", "id": auction.id, "title": auction.title}

# ---------- Listar subastas ----------
@app.get("/auctions/")
def list_auctions(db: Session = Depends(get_db)):
    auctions = db.query(Auction).all()
    return [{"id": a.id, "title": a.title, "price": a.starting_price, "owner": a.owner.username} for a in auctions]
