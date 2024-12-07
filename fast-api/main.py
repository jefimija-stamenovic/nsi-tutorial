from fastapi import FastAPI, APIRouter
from UI.product import router as router_product 
from UI.user import router as router_user 
from UI.recipe import router as router_recipe 

app = FastAPI(
    title = "Napredno softversko inženjerstvo - Tutorial", 
)

app.include_router(router_user)
app.include_router(router_product)
app.include_router(router_recipe)

@app.get("/", status_code = 200)
async def root():
    return {"message": "Hello World!"}


"""if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")"""