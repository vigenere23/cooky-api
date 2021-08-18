from src.infra.db.models.ingredient.ingredient_model import IngredientModel
from src.infra.db.refactor.mysql_condition_builder import MysqlConditionBuilder
from src.infra.db.refactor.mysql_executor import MySQLExecutor


class IngredientDao:

    def __init__(self):
        self.__table_name = 'Ingredient'

    def find_all(self, executor: MySQLExecutor, name: str = None):
        conditions = []
        data = {}

        if name:
            conditions.append("LOWER (name) LIKE LOWER(%(name)s)")
            data['name'] = f'%{name}%'

        condition = MysqlConditionBuilder().where(conditions, data).build()
        results = executor.find_all(self.__table_name, condition)

        return [IngredientModel(**result) for result in results]
