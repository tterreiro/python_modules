#!/usr/bin/env python3

def ft_import_transmutation() -> None:
    print("=== Import Transmutation Mastery ===\n")

    import alchemy.elements
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())

    from alchemy.elements import create_water
    print("\nMethod 2 - Specific function import:")
    print("create_water():", create_water())

    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    print("heal():", heal())

    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print("create_earth():", create_earth())
    print("create_fire():", create_fire())
    print("strength_potion():", strength_potion())

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    ft_import_transmutation()
