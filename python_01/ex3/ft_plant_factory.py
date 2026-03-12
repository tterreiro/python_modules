#!/usr/bin/env python3

class Plant:
    """
    Represents a plant in the garden.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes plant in the garden with name, height and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Prints plant's name, height and age."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    """
    Initializes plants inside the list and displays their attributes
    """
    inventory = [
        Plant("Spathiphyllum", 10, 54), Plant("Zamioculcas", 67, 36),
        Plant("Cannabis", 109, 98), Plant("Tulipa", 27, 21),
        Plant("Anthurium", 75, 674), Plant("Bellis", 15, 49)
    ]
    print("=== Plant Factory Output ===")
    count = 0
    for plant in inventory:
        plant.get_info()
        count += 1
    print("\nTotal plants created:", count)


if __name__ == "__main__":
    ft_plant_factory()
