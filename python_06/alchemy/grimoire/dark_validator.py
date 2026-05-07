from .dark_spellbook import dark_spell_ingredients


def dark_validator(ingredients: str) -> str:
    ingredient_list = ingredients.lower().split(" ")
    for ingredient in ingredient_list:
        if ingredient in dark_spell_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
