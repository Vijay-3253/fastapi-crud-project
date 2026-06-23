"""
Database engine, session factory, and declarative base.

Builds the SQLAlchemy engine safely and configures connection pooling so the
app survives dropped or idle PostgreSQL connections. The public names
`engine`, `SessionLocal`, and `Base` are unchanged, so main.py, the models,
and the dependencies keep working without edits.
"""

import os

from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)


# ---------------------------------
# Connection URL (built safely)
# ---------------------------------
# URL.create() URL-encodes the username and password for us, so a password
# that contains special characters (@ : / # ? and so on) no longer corrupts
# the connection string. It also keeps the credentials structured, which means
# SQLAlchemy prints the password as *** in logs and tracebacks instead of
# leaking it in plain text. (The old f-string did neither.)

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    # config.py validates the other vars but not the port, so default it here.
    port=int(DB_PORT) if DB_PORT else 5432,
    database=DB_NAME,
)


# ---------------------------------
# Engine + connection pool
# ---------------------------------
# pool_pre_ping   : test a pooled connection before using it, so a restarted
#                   or timed-out database doesn't crash the next request.
# pool_recycle    : drop and replace connections older than 30 minutes to avoid
#                   "server closed the connection unexpectedly" errors.
# pool_size /
# max_overflow    : keep 5 connections ready, allow 10 more under load.
# pool_timeout    : wait at most 30s for a free connection before erroring.
# connect_timeout : fail fast (10s) instead of hanging if the DB is unreachable.
# echo            : OFF by default; only logs SQL + parameters when SQL_ECHO=true
#                   is set, so query data never leaks into logs accidentally.

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    echo=os.getenv("SQL_ECHO", "false").strip().lower() == "true",
    connect_args={"connect_timeout": 10},
)


# ---------------------------------
# Session factory
# ---------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# ---------------------------------
# Declarative base for models
# ---------------------------------
# Imported from sqlalchemy.orm. The old sqlalchemy.ext.declarative path is
# deprecated in SQLAlchemy 2.0, which this project uses.

Base = declarative_base()