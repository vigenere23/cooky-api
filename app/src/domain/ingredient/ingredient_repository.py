from abc import ABC, abstractmethod
from typing import List
from src.domain.ingredient.ingredient import Ingredient

class IngredientRepository(ABC):

    @abstractmethod
    def find_all_by_name(self, name: str) -> List[Ingredient]:
        raise NotImplementedError()
