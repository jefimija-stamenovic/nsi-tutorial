from sqlalchemy.orm import Session
from models.user import User
import schemas.user as schema

from models.user import User as UserModel
from models.todo import Todo as TodoModel

def get_user(db: Session, user_id: int) -> UserModel:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
 
def get_users(db: Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schema.UserCreate) -> UserModel:
    db_user = UserModel(email=user.email, name=user.name, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    if user.todos:
        todos = [ TodoModel(title=todo.title, description=todo.description, owner_id=db_user.id) for todo in user.todos]
        db.add_all(todos)
        db.commit()

    db.refresh(db_user)
    return db_user

def delete_user(db: Session, 
                korisnik_za_brisanje: UserModel) -> bool:
    db.delete(korisnik_za_brisanje)
    db.commit()
    return True