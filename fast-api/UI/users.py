from fastapi import APIRouter, HTTPException, Depends
from http import HTTPStatus
from sqlalchemy.orm import Session
from DAL.dependency import get_db
import schemas.user as schemas
import BL.users as service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get('/',
        response_model=list[schemas.User], 
        name="List of all users",
        description="API returns all registrated users."
        )
def get_all_users(skip:int = 0, 
                  limit:int = 100, 
                  db: Session = Depends(get_db)): 
    return service.get_users(db, skip, limit)

@router.get('/{user_id}', 
            response_model=schemas.User, 
            status_code=HTTPStatus.OK, 
            name="Find user by ID", 
            description="API returns user object by ID")
def find_user_by_id(user_id: int, 
                    db: Session = Depends(get_db)) -> schemas.User:
    try:
        user = service.find_user_by_id(db, user_id)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )
    
@router.post('/', 
             response_model = schemas.UserCreate, 
             status_code=HTTPStatus.CREATED, 
             name="Add user", 
             description="The API adds a user and returns an object with information about the new user if it was successfully added")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)

@router.delete('/',  
               status_code=HTTPStatus.NO_CONTENT, 
               name="Delete user", 
               description="The API deletes user by ID")
def delete_user(user_id : int, 
                db: Session = Depends(get_db)): 
    try: 
        service.delete_user(db, user_id)
    except Exception as e: 
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )
    
@router.put("/{user_id}", 
            status_code = HTTPStatus.OK, 
            response_model=schemas.UserUpdate, 
            name = "Update user", 
            description="The API update user by ID")
def update_user(user_id: int, user_data: schemas.UserUpdate, 
                db: Session = Depends(get_db)):
    try:
        updated_user = service.update_user(db, user_id, user_data)
        return updated_user
    except Exception as e: 
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )