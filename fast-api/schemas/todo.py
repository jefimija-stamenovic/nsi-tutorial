from pydantic import BaseModel
from typing import List, Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True