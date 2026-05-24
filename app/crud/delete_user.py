from sqlalchemy.orm import Session

from app.models.user_model import User


# ----------------------------------------
# DELETE USER LOGIC
# ----------------------------------------
def delete_user(db: Session, user_id: int):

    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        return None

    db.delete(existing_user)
    db.commit()

    return existing_user