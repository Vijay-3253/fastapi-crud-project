from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user_model import User
from app.schemas.user_schema import UserUpdate


# ----------------------------------------
# UPDATE USER LOGIC
# ----------------------------------------
def update_user(db: Session, user_id: int, user: UserUpdate):

    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        return None

    if user.name is not None:
        existing_user.name = user.name

    if user.email is not None:
        duplicate_user = (
            db.query(User)
            .filter(User.email == user.email, User.id != user_id)
            .first()
        )

        if duplicate_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )

        existing_user.email = user.email

    if user.password is not None:
        existing_user.password = hash_password(user.password)

    try:
        db.commit()
        db.refresh(existing_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    return existing_user