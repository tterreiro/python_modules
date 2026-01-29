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
        self.age = age
        self.height = height


class Flower(Plant):
    """
    Represents a plant of the flower type in the garden and its development.

    Attributes:
        name (str): The name of the plant.
        height (float): Height in centimeters.
        age (int): Age in days.
        colour (str): The colour of the flower
    """
    def __init__(self, n: str, h: float, a: int, colour: str) -> None:
        """
        Initializes plant in the garden with name, height, age and colour.
        """
        super().__init__(n, h, a)
        self.colour = colour

    def bloom(self) -> None:
        """Ability to bloom (depending on the colour)"""
        if self.colour.lower() == "grey":
            print(self.name.title(), "is blooming beau-, wait.. is it dead?")
        else:
            print(self.name.title(), "is blooming beautifully!")

    def get_info(self) -> None:
        """Displays plant information and executes its unique ability"""
        print(
            f"{self.name.title()} (Flower): {self.height:.1f}cm, "
            f"{self.age} days, {self.colour} colour"
        )
        self.bloom()


class Tree(Plant):
    """
    Represents a plant of the flower type in the garden and its development.

    Attributes:
        name (str): The name of the plant.
        height (float): Height in centimeters.
        age (int): Age in days.
        trunk (float): Tree's trunk diameter in square meters
    """
    def __init__(self, name: str, height: float, age: int, dia: float) -> None:
        """
        Initializes plant in the garden with name, height, age and trunk size.
        """
        super().__init__(name, height, age)
        self.trunk = dia

    def produce_shade(self) -> None:
        """
        Ability to produce shade depending on the trunk size and tree height.
        """
        shade = self.trunk + (self.height / 18)
        print(f"{self.name.title()} provides {shade:.0f} sq meters of shade")

    def get_info(self) -> None:
        """Displays plant information and executes its unique ability"""
        print(
            f"{self.name.title()} (Tree): {self.height:.1f}cm, "
            f"{self.age} days, {self.trunk:.1f} diameter"
        )
        self.produce_shade()


class Vegetable(Plant):
    """
    Represents a plant of the flower type in the garden and its development.

    Attributes:
        name (str): The name of the plant.
        height (float): Height in centimeters.
        age (int): Age in days.
        harv (str): The harvest season of the vegetable.
        nutri (str): The vegetable's nutritional value.
    """
    def __init__(self, n: str, h: float, a: int, har: str, nutri: str) -> None:
        """
        Initializes plant in the garden with name, height, age, harvest season
        and nutritional value.
        """
        super().__init__(n, h, a)
        self.harv = har
        self.nutri = nutri

    def show_nutri(self) -> None:
        """Displays nutritional value"""
        print(self.name.title(), "is rich in", self.nutri)

    def get_info(self) -> None:
        """Displays plant information and executes its unique ability"""
        print(
            f"{self.name.title()} (Vegetable): {self.height:.1f}cm, "
            f"{self.age} days, {self.harv} harvest"
        )
        self.show_nutri()


def ft_plant_types() -> None:
    """Creates a list with all the plants and displays their info"""
    print("=== Garden Plant Types ===")
    inventory = [
        Flower("rose", 25, 30, "red"), Flower("lavender", 12, 94, "grey"),
        Tree("oak", 500, 1825, 50), Tree("maple", 432, 1375, 35),
        Vegetable("tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("lettuce", 101, 73, "spring", "vitamin A")
    ]
    for planty in inventory:
        print("\n")
        planty.get_info()


if __name__ == "__main__":
    ft_plant_types()
