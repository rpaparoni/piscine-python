def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ing_lower = ingredients.lower()
    for a in allowed:
        if a in ing_lower:
            return "VALID"
    return "INVALID"
