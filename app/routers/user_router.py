from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.dependencies.database_dependency import get_db
from app.dependencies.rbac_dependency import require_role
from app.core.rbac import Role
from app.schemas.user_schema import UserUpdate
from app.core.password import hash_password
from app.dependencies.auth_dependency import get_current_user
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ----------------------------------------
# UPDATE USER (ADMIN ONLY)
# ----------------------------------------


@router.put("/{user_id}")
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    # User can update only themselves, admin can update anyone
    if current_user["role"] != "admin" and int(current_user["user_id"]) != user_id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to update this user"
        )

    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.name is not None:
        db_user.name = data.name

    if data.email is not None:
        db_user.email = data.email

    if data.password is not None:
        db_user.password = hash_password(data.password)

    db.commit()
    db.refresh(db_user)

    return {
        "message": "User updated successfully"
    }


# ----------------------------------------
# GET USERS (ADMIN ONLY)
# ----------------------------------------
@router.get("/")
def get_users(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    # Admin → get all users
    if current_user["role"] == "admin":
        users = db.query(User).all()
        return {
            "message": "Admin access",
            "data": users
        }

    # User → get only their own data
    user = db.query(User).filter(
        User.id == int(current_user["user_id"])
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User access",
        "data": user
    }

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role(Role.ADMIN))
):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(db_user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }