
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate


# ----------------------------------------
# UPDATE USER LOGIC
# ----------------------------------------
def update_user(db: Session, user_id: int, user: UserCreate):

    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        return None

    existing_user.name = user.name
    existing_user.email = user.email

    db.commit()
    db.refresh(existing_user)

    return existing_user