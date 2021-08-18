import unittest
from assertpy import assert_that
from src.domain.ingredient.quantity_type import QuantityType


class QuantityTypeTest(unittest.TestCase):

    def test_it_can_create_from_key(self):
        ingredient_type = QuantityType['VOLUME']
        assert_that(ingredient_type).is_equal_to(QuantityType.VOLUME)

    def test_given_invalid_key__it_cannot_create_from_key(self):
        assert_that(lambda: QuantityType['SOMETHING']).raises(KeyError)

    def test_it_can_create_from_value(self):
        ingredient_type = QuantityType('volume')
        assert_that(ingredient_type).is_equal_to(QuantityType.VOLUME)

    def test_given_invalid_value__it_cannot_create_from_value(self):
        assert_that(lambda: QuantityType('something')).raises(ValueError)


if __name__ == '__main__':
    unittest.main()
