from abc import ABC, abstractmethod
from typing import List
from src.domain.recipe.recipe import Recipe
from src.application.recipe.recipe_creation_dto import RecipeCreationDto

class RecipeRepository(ABC):

    @abstractmethod
    def find_by_id(self, recipe_id: int) -> Recipe:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, name: str = None, user_id: int = None) -> List[Recipe]:
        raise NotImplementedError()

    @abstractmethod
    def find_all_liked_by(self, user_id: int) -> List[Recipe]:
        raise NotImplementedError()

    # FUTURE: save domain Recipe instead
    @abstractmethod
    def save(self, recipe: RecipeCreationDto) -> int:
        raise NotImplementedError()

    @abstractmethod
    def replace(self, recipe: Recipe) -> Recipe:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, recipe: Recipe) -> None:
        raise NotImplementedError()
