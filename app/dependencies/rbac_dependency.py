from fastapi import Depends, HTTPException
from app.core.rbac import Role
from app.dependencies.auth_dependency import get_current_user


def require_role(required_role: Role):

    def checker(user: dict = Depends(get_current_user)):

        user_role = user.get("role")

        print("RBAC EXECUTING")
        print("USER ROLE:", user_role)
        print("REQUIRED ROLE:", required_role.value)

        if user_role is None:
            raise HTTPException(
                status_code=403,
                detail="Role missing"
            )

        normalized_user_role = (
            user_role.value if isinstance(user_role, Role) else str(user_role)
        )

        if normalized_user_role != required_role.value:
            raise HTTPException(
                status_code=403,
                detail="Not authorized"
            )

        return user

    return checker