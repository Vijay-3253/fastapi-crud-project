from fastapi import FastAPI

from app.db.database import engine, Base
from app.routers.create_router import router as create_router


# ---------------------------------
# Create Database Tables
# ---------------------------------

Base.metadata.create_all(bind=engine)


# ---------------------------------
# FastAPI Application
# ---------------------------------

app = FastAPI()


# ---------------------------------
# Include Routers
# ---------------------------------

app.include_router(create_router)