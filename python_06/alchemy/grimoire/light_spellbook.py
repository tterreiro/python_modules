def light_spell_ingredients() -> list[str]:
    return ["earth", "air", "water", "fire"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    else:
        return f"Spell recorded: {spell_name} ({validation_result})"
