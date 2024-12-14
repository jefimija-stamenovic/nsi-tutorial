from pydantic import BaseModel, ConfigDict
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str]
    model_config = ConfigDict(from_attributes=True)

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    owner_id: int

class TodoUpdate(TodoBase): 
    pass 