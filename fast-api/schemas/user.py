from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from schemas.todo import Todo, TodoCreate
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(min_length=3, max_length=50)
    
    model_config = ConfigDict(from_attributes=True)

    @field_validator("name")
    def name_validator(cls, name: str): 
        if not name.isalpha(): 
            raise ValueError("Name must contain only alphabetic characters!")
        return name
    
class UserCreate(UserBase):
    todos: List[TodoCreate] = []

class User(UserBase):
    id: int
    is_active: bool = True
    todos: List[Todo] = []

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    is_active: Optional[bool]

    @field_validator("name")
    def name_validator(cls, name: str): 
        if not name.isalpha(): 
            raise ValueError("Name must contain only alphabetic characters!")
        return name