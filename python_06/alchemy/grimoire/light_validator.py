from .light_spellbook import light_spell_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredient_list = ingredients.lower().split(" ")
    for ingredient in ingredient_list:
        if ingredient in light_spell_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
