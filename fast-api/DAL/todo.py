from sqlalchemy.orm import Session
from models.user import User
from models.todo import Todo as TodoModel

import schemas.user as schema

def find_user_by_id(db:Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()
