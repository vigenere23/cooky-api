from dataclasses import dataclass


@dataclass
class IngredientModel:
    id_IngredientType: int
    ingredientType: str
    id_QuantityUnit: int
    name: str
    baseCost: float
    baseQuantity: int = 1
    id: int = None
