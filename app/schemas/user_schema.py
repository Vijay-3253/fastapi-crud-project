from pydantic import BaseModel, EmailStr, Field


# ---------------------------------
# USER CREATE VALIDATION SCHEMA
# ---------------------------------

class UserCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="User full name must be 3-50 characters"
    )

    email: EmailStr   # automatically validates email format