from pydantic import BaseModel
from typing import List, Optional

class RecipeRequest(BaseModel):
    ingredients: List[str]
    diet: Optional[str] = None
    calories: Optional[int] = None

class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    steps: List[str]
    prepTime: str
    calories: int
