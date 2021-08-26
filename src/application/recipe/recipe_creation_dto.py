from dataclasses import dataclass
from typing import List

@dataclass
class RecipeCreationInfo:
    id_User: str
    name: str
    description: str
    directives: str

@dataclass
class RecipeIngredientCreationInfo:
    id_Ingredient: int
    id_QuantityUnit: int
    totalQuantity: int

@dataclass
class RecipeCreationDto:
    recipe: RecipeCreationInfo
    ingredients: List[RecipeIngredientCreationInfo]
