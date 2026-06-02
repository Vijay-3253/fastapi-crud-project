from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.dependencies.auth_dependency import require_role

router = APIRouter(prefix="/users", tags=["Users"])


# 🔐 ONLY ADMIN CAN ACCESS
@router.get("/")
def get_users(
    db: Session = Depends(get_db),
    user=Depends(require_role("ADMIN"))
):
    return {"message": "Admin only data access granted"}