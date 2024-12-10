from pydantic import BaseModel
from schemas.todo import Todo, TodoCreate
from typing import List

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    todos: List[TodoCreate] = []

class User(UserBase):
    id: int
    is_active: bool = True
    todos: List[Todo] = []

    class Config:
        orm_mode = True