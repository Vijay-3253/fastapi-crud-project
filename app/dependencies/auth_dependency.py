from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.core.config import SECRET_KEY, ALGORITHM

# -----------------------------
# JWT SCHEME
# -----------------------------
security = HTTPBearer()


# -----------------------------
# GET CURRENT USER (AUTHENTICATION)
# -----------------------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return {
            "user_id": payload.get("sub"),
            "role": payload.get("role")
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired or invalid"
        )


# -----------------------------
# RBAC (AUTHORIZATION)
# -----------------------------
def require_role(required_role: str):

    def role_checker(user=Depends(get_current_user)):

        user_role = user.get("role")

        if not user_role:
            raise HTTPException(
                status_code=403,
                detail="Role not found in token"
            )

        # 🔥 FIX: case-insensitive comparison
        if user_role.upper() != required_role.upper():
            raise HTTPException(
                status_code=403,
                detail=f"Access denied: {required_role} role required"
            )

        return user

    return role_checker
