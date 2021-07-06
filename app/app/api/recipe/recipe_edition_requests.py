from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RecipeNameEditionRequest:
    name: str

@dataclass_json
@dataclass
class RecipeDirectivesEditionRequest:
    directives: str
