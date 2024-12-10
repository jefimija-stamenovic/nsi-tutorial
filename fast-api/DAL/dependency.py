from database import SessionLocal
from sqlalchemy.orm import Session

# vraca se instanca Context Manager-a
def get_db():
    db = SessionLocal()
    try:
        yield db  # FastAPI koristi `yield` za "context manager"
    finally:
        db.close()