from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ing_lower = ingredients.lower()
    for a in allowed:
        if a in ing_lower:
            return "VALID"
    return "INVALID"
