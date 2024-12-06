from fastapi import APIRouter

class Router(APIRouter):
    pass 
    
router = Router()
@router.get("/users", tags=["Users"])
def get_users(): 
    return [{"id": 1, 
             "name": "Jefimija", 
             "surname": "Stamenovic"}]