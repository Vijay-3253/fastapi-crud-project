from sqlalchemy import Column, Integer, String

from app.db.database import Base


# ---------------------------------
# User Database Model
# ---------------------------------

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)