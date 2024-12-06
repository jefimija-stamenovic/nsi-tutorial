from datetime import date
from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int
    name: str
    surname: str