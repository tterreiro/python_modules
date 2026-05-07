from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    earth_result = create_earth()
    air_result = create_air()
    return f"Healing potion brewed with '{earth_result}' and '{air_result}'"


def strength_potion() -> str:
    fire_result = create_fire()
    water_result = create_water()
    return f"Strength potion brewed with '{fire_result}' and '{water_result}'"
