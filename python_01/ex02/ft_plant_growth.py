#!/usr/bin/env python3


class Plant:
    """
    Represents a plant in the garden and its development.

    Attributes:
        name (str): The name of the plant.
        height (float): Height in centimeters.
        age (int): Age in days.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes plant in the garden with name, height and age."""
        self.name = name
        self.initial_height = height
        self.age = age
        self.height = height

    def get_info(self) -> None:
        """Prints plant's name, height and age."""
        print(f"{self.name.title()}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        """Calculates growth based on the current height-to-age ratio."""
        if self.age > 0 and self.height > 0:
            self.height += self.height / self.age
        elif self.age == 0 or self.height == 0:
            self.height += 1.67

    def get_older(self, time: int) -> None:
        """Increases the plant's age by the specifies number of days."""
        self.age += time


def ft_garden_growth() -> None:
    """Displays a weekly summary of the plant's growth."""
    spathiphyllum = Plant("Spathiphyllum", 10.0, 54)
    zamioculcas = Plant("Zamioculcas", 67.0, 36)
    cannabis = Plant("Cannabis", 109.0, 98)
    inventory = [spathiphyllum, zamioculcas, cannabis]
    for i in range(7):
        print(f"\n=== Day {i + 1} ===")
        for plant in inventory:
            plant.grow()
            plant.get_older(1)
            plant.get_info()
            if i == 6:
                growth = plant.height - plant.initial_height
                print(f"Growth this week: +{growth:.1f}cm\n")


if __name__ == "__main__":
    ft_garden_growth()
