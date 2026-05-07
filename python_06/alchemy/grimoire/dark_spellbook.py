from .dark_validator import dark_validator


def dark_spell_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result = dark_validator(ingredients)
    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    else:
        return f"Spell recorded: {spell_name} ({validation_result})"
