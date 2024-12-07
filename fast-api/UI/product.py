from fastapi import APIRouter

router = APIRouter(tags=["Products"])

@router.get("/products")
def get_products():
    return [{"id": 1, "name": "laptop"}, 
            {"id": 2, "name": "phone"}]

@router.get('/products/{product_id}')
def get_product(product_id: int): 
    return [{"product": "Water"}]