from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate


# ---------------------------------
# Creating User Logic
# ---------------------------------

def create_user(db: Session, user: UserCreate):

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user