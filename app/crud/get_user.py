from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.user_model import User

# ----------------------------------------
# GET ALL USERS LOGIC
# ----------------------------------------
def get_all_users(db: Session):
    return db.query(User).filter(func.lower(User.role) == "user").all()




# ----------------------------------------
# GET USER BY ID LOGIC
# ----------------------------------------
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
