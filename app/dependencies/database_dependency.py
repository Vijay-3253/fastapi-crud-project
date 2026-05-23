from app.db.database import SessionLocal


# ---------------------------------
# Database Dependency Injection
# ---------------------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()