import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Read the secret settings from the .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# The connection to the database
engine = create_engine(DATABASE_URL)

# A factory that makes "sessions" (conversations with the database)
SessionLocal = sessionmaker(bind=engine)


# The parent class for all our tables
class Base(DeclarativeBase):
    pass


# Give each request its own session, then close it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()