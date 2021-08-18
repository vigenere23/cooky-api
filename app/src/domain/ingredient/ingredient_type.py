from enum import Enum


class IngredientType(Enum):
    DAIRY='dairy'
    OIL='oil'
    FRUITS_AND_VEGETABLES='fruits_and_vegetables'
    CONFECTIONERY='confectionery'
    CEREAL='cereal'
    MEAT='meat'
    FISH='fish'
    EGG='egg'
    SPICES='spices'
    BEVERAGE='beverage'
    SALAD='salad'
    PREPARED='prepared'
    OTHER='other'

    @classmethod
    def from_value(cls, value: str):
        return cls(value)

    def describe(self) -> str:
        descriptions = {
            IngredientType.DAIRY: 'Dairy products',
            IngredientType.OIL: 'Oils',
            IngredientType.FRUITS_AND_VEGETABLES: 'Fruits and vegetables',
            IngredientType.CONFECTIONERY: 'Confectionary',
            IngredientType.CEREAL: 'Cereal products',
            IngredientType.MEAT: 'Meat products',
            IngredientType.FISH: 'Fish products',
            IngredientType.EGG: 'Egg products',
            IngredientType.SPICES: 'Spices',
            IngredientType.BEVERAGE: 'Beverages',
            IngredientType.SALAD: 'Salads',
            IngredientType.PREPARED: 'Prepared foods',
            IngredientType.OTHER: 'Others'
        }
        return descriptions[self]
