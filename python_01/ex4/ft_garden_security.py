#!/usr/bin/env python3

class SecurePlant:
    """
    Represents a plant in the garden.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes plant in the garden with name, height and age."""
        self.name = name
        print(f"Plant created: {name}")
        if height < 0:
            print(f"Invalid height input: {height}cm")
            self._height = 0
        else:
            self._height = height
        if age < 0:
            print(f"Invalid age input {age} days")
            self._age = 0
        else:
            self._age = age

    def set_height(self, h: float) -> None:
        """Changes plant height after checking if the input is negative"""
        if h < 0:
            print(f"\nInvalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = h
            print(f"Height updated: {h}cm [OK]")

    def set_age(self, age: int) -> None:
        """Changes plant age after checking if the input is negative"""
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> float:
        """Returns plant's height value"""
        return (self._height)

    def get_age(self) -> int:
        """Returns plant's age value"""
        return (self._age)

    def __str__(self) -> str:
        """Defines what happens when you try to print(plant1)"""
        return f"{self.name} ({self.get_height()}cm, {self.get_age()}"


def ft_garden_security() -> None:
    """Creates plant and tests everything"""
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 53, 81)
    plant1.set_height(25)
    plant1.set_age(30)
    plant1.set_height(-5)
    print(f"Current plant: {plant1} days)")


if __name__ == "__main__":
    ft_garden_security()
