from sqlalchemy.orm import Session
from app.models.user_model import User  # ✅ user_model not user

def update_user(db: Session, user_id: int, name: str, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.name = name
    user.email = email
    db.commit()
    db.refresh(user)
    return user  