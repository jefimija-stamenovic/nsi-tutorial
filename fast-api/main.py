from fastapi import FastAPI, Depends, HTTPException
from database import engine
from UI.users import router as router_user
from UI.todos import router as router_todo
from dotenv import load_dotenv

import uvicorn, os
import models.user as model_user
import models.todo as model_todo

model_user.Base.metadata.create_all(bind=engine)
model_todo.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Napredno softversko inženjerstvo - tutorial")
app.include_router(router_user)
app.include_router(router_todo)

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))