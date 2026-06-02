from app.core.security import verify_password
if not verify_password(user.password, db_user.password):
    raise HTTPException(status_code=401, detail="Invalid credentials")