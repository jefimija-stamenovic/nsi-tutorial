import DAL.todos as db_service
import schemas.todo as schemas
from sqlalchemy.orm import Session
from typing import Sequence 

def get_todo_by_id(db:Session, todo_id: int): 
    return db_service.get_todo_by_id(db, todo_id)

def create_todo(db:Session, new_todo:schemas.Todo) -> Sequence[schemas.Todo]:
    if (not new_todo.title) or (not new_todo.owner_id):
        raise ValueError("Title and owner ID are required!")
    return db_service.create_todo(db, new_todo)

def get_todos(db:Session, owner_id: int):
    return db_service.get_todos(db, owner_id)

def update_todo(db: Session, user_id: int, todo_data: schemas.TodoUpdate) -> schemas.Todo:
    try:
        if (todo_data.description == ""):
            raise Exception("Description cannot be empty.")
        if (todo_data.title == ""):
            raise Exception("Title cannot be empty.")
        update_todo = db_service.update_todo(db, user_id, todo_data.model_dump(exclude_unset=True))
        if not update_todo:
            raise Exception("User not found or update failed.")
        return update_todo
    except Exception as e:
        raise e

def delete_todo(db: Session, todo_id: int) -> schemas.Todo: 
    try:
        todo_for_delete = get_todo_by_id(db, todo_id)
        deleted = db_service.delete_todo(db, todo_for_delete)
        if not deleted: 
            raise Exception(f"An error occurred. Todo with ID {todo_id} has not been deleted")
        return deleted
    except Exception as e: 
        raise e
    