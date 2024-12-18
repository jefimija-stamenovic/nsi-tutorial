from sqlalchemy.orm import Session
from models.user import User
from models.todo import Todo as TodoModel
from typing import Dict, Any

def find_user_by_id(db:Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
 
def get_users(db: Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: Dict[str, Any]) -> User:
    db_user = User(email=user['email'], name=user['name'], is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    if user['todos']:
        todos = [TodoModel(title=todo['title'], description=todo['description'], owner_id=db_user.id) for todo in user['todos']]
        db.add_all(todos)
        db.commit()

    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> bool:
    user_for_delete = find_user_by_id(db, user_id)
    db.delete(user_for_delete)
    db.commit()
    return True

def update_user(db: Session, user_id: int, updated_user: Dict[str, Any]) -> User | None:
    user = find_user_by_id(db, user_id)
    if not user:
        return None
    for key, value in updated_user.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user