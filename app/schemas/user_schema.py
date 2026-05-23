from pydantic import BaseModel


# ---------------------------------
# User Request Schema
# ---------------------------------

class UserCreate(BaseModel):

    name: str
    email: str