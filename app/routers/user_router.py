from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.dependencies.auth_dependency import require_role
from app.crud.get_user import get_all_users

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(
    db: Session = Depends(get_db),
    user=Depends(require_role("ADMIN"))
):
    return {
        "message": "Users fetched successfully",
        "data": get_all_users(db),
        "requested_by": user
    }