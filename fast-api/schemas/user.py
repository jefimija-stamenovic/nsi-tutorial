from pydantic import BaseModel, ConfigDict
from schemas.todo import Todo, TodoCreate
from typing import List, Optional

class UserBase(BaseModel):
    email: str
    name: str
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    todos: List[TodoCreate] = []

class User(UserBase):
    id: int
    is_active: bool = True
    todos: List[Todo] = []

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]