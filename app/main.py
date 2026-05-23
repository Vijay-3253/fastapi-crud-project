from fastapi import FastAPI

from app.db.database import engine, Base
from app.routers.create_router import router as create_router

from app.routers.get_router import router as get_router

from app.routers.update_router import router as update_router 



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
app.include_router(get_router)
#---trupti
app.include_router(update_router) 



