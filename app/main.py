from fastapi import FastAPI

from app.db.database import engine, Base
from app.routers.create_router import router as create_router

from app.routers.get_router import router as get_router

from app.routers.update_router import router as update_router
from app.routers.delete_router import router as delete_router



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

from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router
app.include_router(auth_router)
app.include_router(user_router)
