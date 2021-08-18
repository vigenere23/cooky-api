from dataclasses import asdict
from typing import List
from src.infra.db.refactor.ingredient.ingredient_dao import IngredientDao
from src.domain.ingredient.ingredient import Ingredient
from src.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from src.domain.ingredient.ingredient_repository import IngredientRepository


class MySQLIngredientRepository(IngredientRepository):

    def __init__(
        self,
        db_connection: MysqlDBConnection,
        ingredient_dao: IngredientDao
    ):
        self.__db_connection = db_connection
        self.__ingredient_dao = ingredient_dao

    def find_all_by_name(self, name: str) -> List[Ingredient]:
        with self.__db_connection.transaction() as executor:
            results = self.__ingredient_dao.find_all(executor, name)
            return [Ingredient(**asdict(result)) for result in results]
