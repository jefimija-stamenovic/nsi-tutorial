from sqlalchemy.orm import Session
from models.todo import Todo
from typing import Sequence 

def create_todo(db:Session, todo:Todo) -> Todo:
    new_todo = Todo(title=todo.title, description=todo.description, owner_id=todo.owner_id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_todos(db:Session, owner_id: int) -> Sequence[Todo]:
    return db.query(Todo).filter(Todo.owner_id == owner_id).all()

def get_todo_by_id(db:Session, todo_id: int) -> Todo:
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo_id: int, updated_todo: Todo) -> Todo:
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        return None
    for key, value in updated_todo.items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_for_delete: Todo) -> bool:
    db.delete(todo_for_delete)
    db.commit()
    return True