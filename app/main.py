from fastapi import FastAPI
from .database import Base, engine
from .routers import drives

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Drive Management API")

app.include_router(drives.router)