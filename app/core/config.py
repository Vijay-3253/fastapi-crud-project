import os
from dotenv import load_dotenv

load_dotenv()


# ---------------------------------
# Database Environment Variables
# ---------------------------------

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
# VALIDATION (IMPORTANT)
# -----------------------------
if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
    raise Exception(":x: Database configuration is missing in .env file")

# -----------------------------
# JWT CONFIG
# -----------------------------
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise Exception(":x: SECRET_KEY is missing in .env file")

ALGORITHM = os.getenv("ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15)
)

REFRESH_TOKEN_EXPIRE_DAYS = int(
    os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7)
)