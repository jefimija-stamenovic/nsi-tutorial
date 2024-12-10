from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas.todo as schemas
import crud, models

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()
router = APIRouter(prefix="/todo", tags=["Todos"])

@router.get("/", response_model=list[schemas.Todo])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = crud.get_todos(db,skip=skip,limit=limit)
    return todos