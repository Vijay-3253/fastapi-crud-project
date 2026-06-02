from sqlalchemy import Column, Integer, String
from app.db.database import Base

# ---------------------------------
# User Database Model
# ---------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    role = Column(String(20), default="USER")