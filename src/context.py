import logging
from src.mysql_connection import connect_to_mysql
from src.infra.db.mysql_database_connection import MySQLDBConnection
from src.infra.db.db_connector import DBConnector
from src.infra.db.sql_transaction import SQLTransaction
from src.infra.db.refactor.mysql_db_connection import MysqlDBConnection
from src.infra.db.refactor.recipe.mysql_recipe_repository import MySQLRecipeRepository
from src.infra.db.refactor.recipe.recipe_dao import RecipeDao
from src.infra.db.refactor.recipe.recipe_ingredient_dao import RecipeIngredientDao
from src.infra.db.refactor.user.address_dao import AddressDao
from src.infra.db.refactor.user.user_dao import UserDao
from src.infra.db.refactor.user.account_dao import AccountDao
from src.infra.db.refactor.user.mysql_user_repository import MysqlUserRepository
from src.application.recipe.recipe_editing_usecase import RecipeEditingUseCase
from src.application.authentication import AuthenticationUseCase
from src.application.account.user_finding_usecase import UserFindingUseCase
from src.application.recipe.recipe_finding_usecase import RecipeFindingUseCase
from src.application.recipe.recipe_creation_usecase import RecipeCreationUseCase
from src.application.account.signup_usecase import SignupUseCase
from src.application.account.user_editing_usecase import UserEditingUseCase


logger = logging.getLogger('gunicorn.error')
mysql_connection = connect_to_mysql()

db_connection = MySQLDBConnection(mysql_connection)
db = DBConnector(db_connection)
transaction = SQLTransaction(db_connection)

db_connection_2 = MysqlDBConnection(mysql_connection)
recipe_repository = MySQLRecipeRepository(db_connection_2, RecipeDao(), RecipeIngredientDao())
user_repository = MysqlUserRepository(db_connection_2, AccountDao(), UserDao(), AddressDao())

authentication_use_case = AuthenticationUseCase(user_repository)
recipe_creation_usecase = RecipeCreationUseCase(recipe_repository)
recipe_finding_usecase = RecipeFindingUseCase(recipe_repository)
recipe_editing_usecase = RecipeEditingUseCase(authentication_use_case, recipe_repository)
signup_usecase = SignupUseCase(user_repository)
user_finding_usecase = UserFindingUseCase(user_repository)
user_editing_usecase = UserEditingUseCase(user_repository)
