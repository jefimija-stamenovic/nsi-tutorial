from fastapi import FastAPI, APIRouter
from UI.product import router as router_product 
from UI.user import router as router_user 

app = FastAPI()

app.include_router(router_user)
app.include_router(router_product)

@app.get("/")
async def root():
    return {"message": "Hello World!"}