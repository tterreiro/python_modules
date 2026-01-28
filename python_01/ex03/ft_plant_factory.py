#!/usr/bin/env python3

class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): The name of the plant.
        height (float): Height in centimeters.
        age (int): Age in days.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes plant in the garden with name, height and age."""
        self.name = name
        self.height = height
        self.age = age
