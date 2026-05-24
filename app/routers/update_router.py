from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.schemas.user_schema import UserCreate
from app.crud.update_user import update_user


# ----------------------------------------
# UPDATE ROUTER
# ----------------------------------------
router = APIRouter()


# ----------------------------------------
# UPDATE USER API
# ----------------------------------------
@router.put("/users/{user_id}")
def update_user_api(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db)
):

    updated_user = update_user(db, user_id, user)

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User updated successfully",
        "data": updated_user
    }