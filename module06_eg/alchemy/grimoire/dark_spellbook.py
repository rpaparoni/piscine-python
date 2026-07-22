from typing import List
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> List[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    status = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} - {status})"
