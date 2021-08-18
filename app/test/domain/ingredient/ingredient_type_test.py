import unittest
from assertpy import assert_that
from src.domain.ingredient.ingredient_type import IngredientType


class IngredientTypeTest(unittest.TestCase):

    def test_it_can_create_from_key(self):
        ingredient_type = IngredientType['MEAT']
        assert_that(ingredient_type).is_equal_to(IngredientType.MEAT)

    def test_given_invalid_key__it_cannot_create_from_key(self):
        assert_that(lambda: IngredientType['SOMETHING']).raises(KeyError)

    def test_it_can_create_from_value(self):
        ingredient_type = IngredientType('meat')
        assert_that(ingredient_type).is_equal_to(IngredientType.MEAT)

    def test_given_invalid_value__it_cannot_create_from_value(self):
        assert_that(lambda: IngredientType('something')).raises(ValueError)

    def test_it_can_get_description(self):
        ingredient_type = IngredientType.MEAT
        description = ingredient_type.describe()

        assert_that(description).is_equal_to('Meat products')


if __name__ == '__main__':
    unittest.main()
