from fastapi import FastAPI
from database import engine
from UI.users import router as router_user
from UI.todos import router as router_todo
from dotenv import load_dotenv
import models.user as model_user
import models.todo as model_todo
import os 

model_user.Base.metadata.create_all(bind=engine)
model_todo.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Napredno softversko inženjerstvo - FastAPI tutorial")
app.include_router(router_user)
app.include_router(router_todo)

load_dotenv()

@app.get("/")
def read_root():
    return {"message": "Hello, this is tutorial for FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)