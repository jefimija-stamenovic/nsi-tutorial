import DAL.users as db_service
from fastapi import Depends
from sqlalchemy.orm import Session
import schemas.user as schemas
from typing import Sequence

from models.user import User as UserModel
from models.todo import Todo as TodoModel
from schemas.user import UserCreate, User

def get_users(db: Session, 
              skip:int=0, 
              limit:int=100) -> Sequence[schemas.User]:
    return db_service.get_users(db, skip, limit)

def get_user_by_id(db: Session, 
                   user_id: int): 
    result = db_service.get_user(db, user_id)
    if not result: 
        message = f"Korisnik čiji je ID = {user_id} nije pronađen!"
        raise Exception(message)
    return 

def get_user_by_email(db: Session, 
                      user_email : str): 
    return db_service.get_user_by_email(db, user_email)

def create_user(db: Session, 
                user: schemas.UserCreate): 
    if (user.name == ''):
        raise Exception("Korisnik mora imati uneto ime")

    if (user.email == ''): 
        raise Exception("Korisnik mora imati unetu email adresu")
    
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise Exception("Korisnik sa ovim email-om je vec registrovan")
    
    return db_service.create_user(db, user)

def delete_user(db: Session, 
                korisnik_id: int): 
    result = True 
    try: 
        result = db_service.delete_user(db, korisnik_id) 
        result = False
    except Exception as e: 
        raise Exception(str(e))
    return result 
