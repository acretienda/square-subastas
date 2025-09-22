from fastapi import FastAPI
from database import Base, engine
from routers import users, auctions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Square Auctions")

app.include_router(users.router)
app.include_router(auctions.router)
