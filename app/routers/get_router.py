from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.crud.get_user import get_all_users, get_user_by_id

# ----------------------------------------
# GET USER ROUTER
# ----------------------------------------
router = APIRouter()



# ----------------------------------------
# GET ALL USERS
# ----------------------------------------
@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users



# ----------------------------------------
# GET USER BY ID
# ----------------------------------------
@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user