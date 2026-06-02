from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str
    role: str

    # 🔐 PASSWORD VALIDATION
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):

        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters long")

        if v.isdigit():
            raise ValueError("Password cannot be only numbers")

        return v


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True