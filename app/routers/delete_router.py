from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.crud.delete_user import delete_user


# ----------------------------------------
# DELETE ROUTER
# ----------------------------------------
router = APIRouter()


# ----------------------------------------
# DELETE USER API
# ----------------------------------------
@router.delete("/users/{user_id}")
def delete_user_api(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted_user = delete_user(db, user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }