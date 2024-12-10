from sqlalchemy.orm import Session
import models
import schemas.todo as schemas

def get_todos(db: Session, skip:int=0, limit: int=100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_user_todo(db:Session, todo:schemas.TodoCreate, user_id : int):
    db_todo = models.Todo(**todo.model_dump(),owner_id=user_id )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo