#!/usr/bin/env python3

class Plant:
    """Represents a plant in the garden."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initializes plant in the garden."""
        self.name = name
        self.age = age
        self.height = height
        self.type = "regular"

    def get_stats(self) -> str:
        """Returns plant info."""
        return f"{self.name}: {self.height:.1f}cm"


class FloweringPlant(Plant):
    """Represents a flowering plant in the garden."""

    def __init__(self, n: str, h: float, a: int, clr: str) -> None:
        """Initializes plant in the garden."""
        super().__init__(n, h, a)
        self.clr = clr
        self.type = "flowering"

    def get_stats(self) -> str:
        """Returns plant information."""
        return (
            f"{self.name}: {self.height:.1f}cm, "
            f"{self.clr} flowers (blooming)"
            )


class PrizeFlower(FloweringPlant):
    """Represents a prize flower in the garden."""

    def __init__(self, n: str, h: float, a: int, clr: str, point: int) -> None:
        """Initializes plant in the garden."""
        super().__init__(n, h, a, clr)
        self.point = point
        self.type = "prize flowers"

    def get_stats(self) -> str:
        """Returns plant information."""
        return f"{super().get_stats()}, Prize points: {self.point}"


class Garden:
    """Represents a garden"""

    def __init__(self, name: str) -> None:
        """Initializes plant in the garden."""
        self.name = name
        self.plants = []
        self.plants_amount = 0
        self.garden_growth = 0

    def get_name(self) -> str:
        """Returns name."""
        return self.name

    def add_plant(self, plant: Plant) -> None:
        """Adds plant to garden."""
        self.plants.append(plant)
        if self != j_garden:
            print(f"Added {plant.name} to {self.name}'s garden")
        self.plants_amount += 1

    def get_growth(self) -> int:
        """Returns growth."""
        return self.garden_growth


class GardenManager:
    """Manages gardens and coordinates with the analytics helper."""

    class GardenStats:
        """Nested helper for calculating garden statistics."""

        @staticmethod
        def calc_height(garden: "Garden") -> float:
            """Calculates height"""
            height = 0
            for x in garden.plants:
                height += x.height
            return height

        @staticmethod
        def validate_height(garden: "Garden") -> bool:
            """Checks for negative heights."""
            for x in garden.plants:
                if x.height < 0:
                    return False
            return True

        @staticmethod
        def grow_garden(garden: "Garden", days: int) -> None:
            """Simulates growth over a set amount of days."""
            print(f"\n{garden.get_name()} is helping all the plants grow...")
            for x in garden.plants:
                growth_amount = 0
                for _ in range(days):
                    if x.age > 0 and x.height > 0:
                        growth_amount += x.height / x.age
                        garden.garden_growth += x.height / x.age
                        x.height += x.height / x.age
                    elif x.age == 0 or x.height == 0:
                        x.height += 1.67
                        garden.garden_growth += 1.67
                        growth_amount += 1.67
                print(f"{x.name} grew {growth_amount:.1f}cm")

        @staticmethod
        def garden_info(garden: "Garden") -> None:
            """Displays the full analytics report for a specific garden."""
            print(f"\n=== {garden.get_name()}'s Garden Report ===")
            print("Plants in garden:")
            for x in garden.plants:
                print(f"- {x.get_stats()}")
            print(
                f"\nPlants added: {garden.plants_amount},"
                f" Total growth: {garden.get_growth():.1f}cm"
                )
            regular = 0
            flowering = 0
            prize_flower = 0
            for x in garden.plants:
                if x.type == "regular":
                    regular += 1
                elif x.type == "flowering":
                    flowering += 1
                else:
                    prize_flower += 1
            print(
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, {prize_flower} prize flowers\n"
                )
            is_valid = GardenManager.GardenStats.validate_height(garden)
            print(f"Height validation test: {is_valid}")

        @staticmethod
        def get_garden_score(garden: "Garden") -> float:
            """Calculates the total score of a garden based on plant heights"""
            score = 0
            for x in garden.plants:
                score += x.height
            return score

    def __init__(self, owner: str) -> None:
        """Initializes the GardenManager with an owner and a garden registry"""
        self.owner = owner
        self.gardens = {}

    def create_garden(self, garden_name: str) -> Garden:
        """Creates a new Garden instance and adds it to the registry."""
        new_garden = Garden(garden_name)
        self.gardens[garden_name] = new_garden
        return new_garden

    def garden_amount(self) -> int:
        """Returns the total number of gardens currently managed."""
        amount = 0
        for x in self.gardens:
            amount += 1
        return amount

    def print_gardens(self) -> None:
        """Prints the dictionary of managed gardens."""
        print(self.gardens)

    @classmethod
    def create_garden_network(cls, admin_name: str) -> "GardenManager":
        """Factory method to initialize the global garden network."""
        print("=== Garden Managements System Demo ===\n")
        return cls(admin_name)


if __name__ == "__main__":
    GM = GardenManager.create_garden_network("admin")

    c_garden = GM.create_garden("Charlie")
    j_garden = GM.create_garden("Jeffy")

    c_garden.add_plant(Plant("Oak Tree", 500, 1825))
    c_garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    c_garden.add_plant(PrizeFlower("Sunflower", 15, 25, "yellow", 67))

    GardenManager.GardenStats.grow_garden(c_garden, 6)
    GardenManager.GardenStats.garden_info(c_garden)

    j_garden.add_plant(Plant("Oak Tree", 264, 1302))
    j_garden.add_plant(FloweringPlant("Cannabis", 109, 98, "green"))
    j_garden.add_plant(PrizeFlower("Lavender", 12, 94, "purple", 41))
    j_garden.add_plant(PrizeFlower("Sunflower", 15, 25, "yellow", 67))

    print(
        f"Garden scores - {c_garden.name}: "
        f"{GardenManager.GardenStats.get_garden_score(c_garden):.0f}, "
        f"{j_garden.name}: "
        f"{GardenManager.GardenStats.get_garden_score(j_garden):.0f}"
        )
    print(f"Total gardens managed: {GM.garden_amount()}")
