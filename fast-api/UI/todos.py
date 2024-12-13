from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import schemas.todo as schemas
from DAL.dependency import get_db
import BL.todos as service
from http import HTTPStatus

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/todos/user/{owner_id}")
def get_todos(owner_id: int, db: Session = Depends(get_db)):
    return service.get_todos(db, owner_id)

@router.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    return service.get_todo_by_id(db, todo_id)

@router.put("/{user_id}", 
            status_code = HTTPStatus.OK, 
            response_model=schemas.TodoUpdate, 
            name = "Update todo", 
            description="The API update todo by ID")
def update_todo(todo_id: int, todo_data: schemas.TodoUpdate, 
                db: Session = Depends(get_db)):
    try:
        updated_todo = service.update_todo(db, todo_id, todo_data)
        return updated_todo
    except Exception as e: 
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )
    
@router.delete('/',  
               status_code=HTTPStatus.NO_CONTENT, 
               name="Delete todo", 
               description="The API deletes todo by ID")
def delete_todo(todo_id : int, 
                db: Session = Depends(get_db)): 
    try: 
        service.delete_todo(db, todo_id)
    except Exception as e: 
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )