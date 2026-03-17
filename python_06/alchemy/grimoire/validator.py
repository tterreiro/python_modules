def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ['fire', 'water', 'earth', 'air']
    ingredient_list = ingredients.split(" ")
    for ingredient in ingredient_list:
        if ingredient not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
