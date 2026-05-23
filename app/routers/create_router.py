from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.schemas.user_schema import UserCreate
from app.crud.create_user import create_user


# ---------------------------------
# Create User Router
# ---------------------------------

router = APIRouter()


@router.post("/users")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(db, user)