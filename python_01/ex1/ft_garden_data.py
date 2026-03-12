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

    def display(self) -> None:
        """Prints plant's stats to the console"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """Creates a list of plants and displays their info"""
    spathiphyllum = Plant("Spathiphyllum", 10, 54)
    zamioculcas = Plant("Zamioculcas", 67, 32)
    cannabis = Plant("Cannabis", 109, 121)
    inventory = [spathiphyllum, zamioculcas, cannabis]
    for plant in inventory:
        plant.display()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
