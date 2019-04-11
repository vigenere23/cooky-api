from app import db
from .model import QuantityUnitModel
from app.helpers.BaseDao import BaseDao

class QuantityUnitDao(BaseDao):

    def __init__(self):
        super().__init__('QuantityUnit', QuantityUnitModel)

    def save(self, quantityUnitModel):
        if not isinstance(quantityUnitModel, QuantityUnitModel):
            raise ValueError("quantityUnitModel should be of type QuantityUnitModel")
        pass

    def getAllQuantityUnitsByIngredientId(self, ingredient_id):
        query = 'SELECT * FROM QuantityUnit U WHERE U.id_QuantityType = (SELECT U2.id_QuantityType FROM QuantityUnit U2, Ingredient I WHERE I.id = %(ingredient_id)s AND I.id_QuantityUnit = U2.id)'
        data = { 'ingredient_id': ingredient_id }
        results = db.select(query, data)
        return self._mapper.from_tuples(results)
