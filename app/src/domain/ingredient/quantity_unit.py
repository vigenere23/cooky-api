from enum import Enum
from src.domain.ingredient.quantity_type import QuantityType


class QuantityUnit(Enum):
    TEASPOON='teaspoon'
    TABLESPOON='tablespoon'
    FLUID_ONCE='fluid ounce'
    CUP='cup'
    MILLILITER='milliliter'
    LITER='liter'
    DECILITER='deciliter'
    POUND='pound'
    OUNCE='ounce'
    MILLIGRAM='milligram'
    GRAM='gram'
    KILOGRAM='kilogram'
    UNIT='unit'

    def abbreviation(self):
        abbreviations = {
            QuantityUnit.TEASPOON: 'tsp',
            QuantityUnit.TABLESPOON: 'tbsp',
            QuantityUnit.FLUID_ONCE: 'fl oz',
            QuantityUnit.CUP: 'cup',
            QuantityUnit.MILLILITER: 'mL',
            QuantityUnit.LITER: 'L',
            QuantityUnit.DECILITER: 'dL',
            QuantityUnit.POUND: 'lb',
            QuantityUnit.OUNCE: 'oz',
            QuantityUnit.MILLIGRAM: 'mg',
            QuantityUnit.GRAM: 'g',
            QuantityUnit.KILOGRAM: 'kg',
            QuantityUnit.UNIT: 'unit'
        }
        return abbreviations[self]

    @classmethod
    def for_type(cls, type: QuantityType):
        if type is QuantityType.VOLUME:
            return [
                cls.TEASPOON,
                cls.TABLESPOON,
                cls.FLUID_ONCE,
                cls.CUP,
                cls.MILLILITER,
                cls.LITER,
                cls.DECILITER
            ]
        elif type is QuantityType.WEIGHT:
            return [
                cls.POUND,
                cls.OUNCE,
                cls.MILLIGRAM,
                cls.GRAM,
                cls.KILOGRAM
            ]
        elif type is QuantityType.UNIT:
            return [cls.UNIT]
        else:
            return []
