from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate


# ---------------------------------
# Creating User Logic
# ---------------------------------

def create_user(db: Session, user: UserCreate):

    try:

        # ---------------------------------
        # Check Existing User
        # ---------------------------------

        existing_user = db.query(User).filter(
            User.email == user.email
        ).first()

        # ---------------------------------
        # User Already Exists
        # ---------------------------------

        if existing_user:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists"
            )

        # ---------------------------------
        # Create New User Object
        # ---------------------------------

        new_user = User(
            name=user.name,
            email=user.email
        )

        db.add(new_user)

        db.commit()

        db.refresh(new_user)

        return new_user

    except HTTPException as http_error:

        raise http_error

    except Exception as error:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database Error: {str(error)}"
        )