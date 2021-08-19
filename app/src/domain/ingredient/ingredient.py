from src.domain.ingredient.ingredient_type import IngredientType


class Ingredient:
    def __init__(
        self,
        id_IngredientType: int,
        ingredientType: str,
        id_QuantityUnit: int,
        # quantityUnit: str,
        name: str,
        baseCost: float,
        baseQuantity: int = 1,
        id: int = None
    ):
        self.id_IngredientType = id_IngredientType
        self.ingredientType = IngredientType(ingredientType)
        self.id_QuantityUnit = id_QuantityUnit
        # self.quantityUnit = QuantityUnit(quantityUnit)
        self.name = name
        self.baseCost = baseCost
        self.baseQuantity = baseQuantity
        self.id = id
