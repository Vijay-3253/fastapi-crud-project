from pydantic import BaseModel, EmailStr, Field, field_validator

from app.core.rbac import Role
class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str
    role: str = "user"   # keep as string for control

    @field_validator("role")
    @classmethod
    def validate_role(cls, v):

        allowed_roles = [role.value for role in Role]

        if v not in allowed_roles:
            raise ValueError(f"Invalid role: {v} is not allowed")

        return v
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
    role: Role = Role.USER
    class Config:
        from_attributes = True
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None