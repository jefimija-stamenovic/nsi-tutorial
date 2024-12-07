from fastapi import APIRouter, HTTPException
from typing import Optional
from DTO.recipe import Recipe, RecipeSearchResults, RecipeCreate
from http import HTTPStatus

router = APIRouter(tags=["Recipes"])
recipes = [
    {
        "id": 1,
        "name": "Chicken Vesuvio",
        "source": "Serious Eats",
        "link": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "name": "Chicken Paprikash",
        "source": "No Recipes",
        "link": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "name": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "link": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]

@router.get('/recipes')
def get_recipes(): 
    return recipes

@router.get('/recipes/{recipe_id}', 
            status_code = HTTPStatus.OK, 
            response_model=Recipe)
def get_recipe(recipe_id:int) -> dict:
    result = [recipe for recipe in recipes if recipe["id"] == recipe_id]
    if not result : 
        raise HTTPException(
            status_code = 404, 
            detail=f"Recipe with ID = {recipe_id} not found"
        )
    return result[0]

@router.get('/recipe/search/', 
    status_code = HTTPStatus.OK, 
    response_model = RecipeSearchResults)
def search_recipes(keyword: Optional[str] = None, 
                    max_results: Optional[int] = 10) -> dict:
    if not keyword:
        return {"results": recipes[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), recipes)  # 7
    return {"results": recipes[:max_results]}

@router.post("/recipe", 
    status_code = HTTPStatus.CREATED, 
    response_model = Recipe)
def create_recipe(new_recipe: RecipeCreate) -> dict: 
    new_entry_id = len(recipes) + 1
    recipe_entry = Recipe(
        id = new_entry_id, 
        name = new_recipe.name, 
        source = new_recipe.source, 
        link = new_recipe.link
    ) 
    recipes.append(recipe_entry.dict())
    return recipe_entry