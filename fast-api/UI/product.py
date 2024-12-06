from fastapi import APIRouter

router = APIRouter()

@router.get("/products", tags=["Products"])
def get_products():
    return [{"id": 1, "name": "laptop"}, 
            {"id": 2, "name": "phone"}]