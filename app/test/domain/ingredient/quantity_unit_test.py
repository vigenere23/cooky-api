from src.domain.ingredient.quantity_type import QuantityType
from src.domain.ingredient.quantity_unit import QuantityUnit
import unittest
from assertpy import assert_that


class QuantityUnitTest(unittest.TestCase):

    def test_it_can_create_from_key(self):
        quantity_unit = QuantityUnit['LITER']
        assert_that(quantity_unit).is_equal_to(QuantityUnit.LITER)

    def test_given_invalid_key__it_cannot_create_from_key(self):
        assert_that(lambda: QuantityUnit['SOMETHING']).raises(KeyError)

    def test_it_can_create_from_value(self):
        quantity_unit = QuantityUnit('liter')
        assert_that(quantity_unit).is_equal_to(QuantityUnit.LITER)

    def test_it_can_list_for_quantity_type(self):
        quantity_units = QuantityUnit.for_type(QuantityType.VOLUME)
        assert_that(quantity_units).contains(QuantityUnit.FLUID_ONCE)

    def test_given_invalid_value__it_cannot_create_from_value(self):
        assert_that(lambda: QuantityUnit('something')).raises(ValueError)

    def test_it_can_get_abbreviation(self):
        quantity_unit = QuantityUnit.LITER
        abbreviation = quantity_unit.abbreviation()

        assert_that(abbreviation).is_equal_to('L')


if __name__ == '__main__':
    unittest.main()
