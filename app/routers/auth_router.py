from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.models.user_model import User
from app.schemas.auth_schema import LoginSchema, TokenResponse, RefreshSchema
from app.core.password import verify_password
from app.core.jwt_token import (
    create_access_token,
    create_refresh_token,
    decode_token
)
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/auth", tags=["Auth"])


# LOGIN
@router.post("/login", response_model=TokenResponse)
def login(user: LoginSchema, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": str(db_user.id),
            "role": db_user.role,
            "type": "access"
        },
        ACCESS_TOKEN_EXPIRE_MINUTES
    )

    refresh_token = create_refresh_token(
        {
            "sub": str(db_user.id),
            "role": db_user.role,
            "type": "refresh"
        }
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# REFRESH TOKEN
@router.post("/refresh")
def refresh(data: RefreshSchema):

    payload = decode_token(data.refresh_token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=401,
            detail="Not a refresh token"
        )

    new_access_token = create_access_token(
        {
            "sub": payload["sub"],
            "role": payload.get("role", "USER"),
            "type": "access"
        },
        ACCESS_TOKEN_EXPIRE_MINUTES
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }