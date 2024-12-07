from pydantic import BaseModel, HttpUrl
from typing import Sequence 

"""
   Sequence je apstraktni tip podataka za označavanje tipova podataka 
   koji predstavljaju sekvence kao što su liste, torke ili bilo koji drugi 
   tip koji podržava indeksiranje i prebrojavanje elemenata
"""


class Recipe(BaseModel): 
    id: int 
    name : str
    source : str 
    link : HttpUrl  


class RecipeSearchResults(BaseModel): 
    results : Sequence[Recipe]

class RecipeCreate(BaseModel): 
    name: str
    source: str
    link: HttpUrl
    added_by: int