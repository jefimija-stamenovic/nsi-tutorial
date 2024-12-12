from pydantic import BaseModel, ConfigDict
from schemas.todo import Todo, TodoCreate
from typing import List, Optional

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    todos: List[TodoCreate] = []
    model_config = ConfigDict(from_attributes=True)

class User(UserBase):
    id: int
    is_active: bool = True
    todos: List[Todo] = []
    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]

    model_config = ConfigDict(from_attributes=True)