from fastapi import APIRouter, HTTPException, Depends
from http import HTTPStatus
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas.user as schemas
import BL.users as service
from DAL.dependency import get_db
from schemas.user import UserCreate

router = APIRouter(prefix="/korisnici", tags=["Korisnici"])

@router.get('/',
        response_model=list[schemas.User], 
        name="Lista svih korisnika",
        description="API vraća listu svih korisnika"
        )
def get_all_users(skip:int = 0, 
                  limit:int = 100, 
                  db: Session = Depends(get_db)): 
    return service.get_users(db, skip, limit)

@router.get('/{korisnik_id}', 
            response_model=schemas.User, 
            status_code=HTTPStatus.OK, 
            name="Pronađi korisnika na osnovu ID-a", 
            description="API vraća objekat sa podacima o korisniku " + 
                        "čiji je ID prosleđen kao parametar")
def find_user_by_id(korisnik_id:int, 
                    db: Session = Depends(get_db)): 
    result = None
    try: 
        result = service.get_user_by_id(db, korisnik_id)
    except Exception as e: 
        raise HTTPException(
            status_code = HTTPStatus.NOT_FOUND, 
            detail=str(e)
        )

@router.post('/', 
             response_model = schemas.UserCreate, 
             status_code=HTTPStatus.CREATED, 
             name="Dodaj novog korisnika", 
             description="API dodaje novog korisnika i vraća objekat " +
             "sa informacijima o novom korisniku ukoliko je uspešno dodat")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    try: 
        return service.create_user(db, user)
    except Exception as e: 
        return HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, 
            detail=str(e)
        )

@router.delete('/', 
               response_model=schemas.UserBase, 
               status_code=HTTPStatus.OK)
def delete_user(korisnik_id : int, 
                db: Session = Depends(get_db)) -> schemas.User: 
    result = service.delete_user(db, korisnik_id)