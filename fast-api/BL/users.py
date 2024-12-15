import DAL.users as db_service
import schemas.user as schemas
from sqlalchemy.orm import Session
from typing import Sequence

def get_users(db: Session, 
              skip:int=0, 
              limit:int=100) -> Sequence[schemas.User]:
    return db_service.get_users(db, skip, limit)

def find_user_by_id(db: Session, user_id: int) -> schemas.User:
    user = db_service.find_user_by_id(db, user_id)
    if user == None: 
        raise Exception(f"User with ID {user_id} not found")
    return user
    
def get_user_by_email(db: Session, 
                      user_email : str): 
    return db_service.get_user_by_email(db, user_email)

def create_user(db: Session, user: schemas.UserCreate):
    if (user.name == ''):
        raise Exception("User must have name!")
    if (user.email == ''): 
        raise Exception("User must have email!")
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise Exception("There has been already registrated user with this email")
    return db_service.create_user(db, user.model_dump(exclude_unset=False))
    #return db_service.create_user(db, user)

def delete_user(db: Session, user_id: int) -> int: 
    try:
        deleted = db_service.delete_user(db, user_id)
        if not deleted: 
            raise Exception(f"An error occurred. User with ID {user_id} has not been deleted")
        return deleted
    except Exception as e: 
        raise e
    
def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    try:
        if (user_data.name == ""):
            raise Exception("Name cannot be empty.")
        if (user_data.email == ""):
            raise Exception("Email cannot be empty.")
        updated_user = db_service.update_user(db, user_id, user_data.model_dump(exclude_unset=True))
        if not updated_user:
            raise Exception("User not found or update failed.")
        return updated_user
    except Exception as e:
        raise e