#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight: int) -> None:
        self.name = name
        self.water_l = water_level
        self.sun_h = sunlight

    def check_health(self) -> str:
        water = self.water_l
        if self.water_l > 10:
            raise ValueError(f"Water level {self.water_l} too high (max 10)")
        elif self.water_l < 1:
            raise ValueError(f"Water level {self.water_l} is too low (min 1)")
        if self.sun_h > 12:
            raise ValueError(f"Sun hours {self.sun_h} is too high (max 12)")
        elif self.sun_h < 2:
            raise ValueError(f"Sunlight hours {self.sun_h} too low (min 2)")
        return f"{self.name}: healthy (water: {water}, sun: {self.sun_h})"


class GardenManager:
    def __init__(self) -> None:
        self.plants = []
        self.water_tank = 15

    def add_plant(self, plant: Plant) -> None:
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        if plant.name in self.plants:
            raise PlantError("Plant already in the garden!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully!")

    def water_plants(self, quantity: int) -> None:
        print("Opening watering system..")
        for plant in self.plants:
            if self.water_tank < quantity:
                raise GardenError("Not enough water in tank")
            plant.water_l += quantity
            self.water_tank -= quantity
            print(f"Watering {plant.name} - success")

    def check_plant_health(self) -> None:
        for plant in self.plants:
            try:
                check = plant.check_health()
                print(check)
            except ValueError as e:
                print(f"Error checking {plant.name}: {e}\n")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    gm = GardenManager()
    plants = [Plant("tomato", 5, 8), Plant("lettuce", 15, 7), Plant("", 5, 5)]

    print("Adding plants to garden...")
    for plant in plants:
        try:
            gm.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}\n")

    print("\nWatering plants...")
    try:
        gm.water_plants(3)
    except WaterError as e:
        print(f"Error watering plant: {e}\n")
    finally:
        print("Closing watering system (cleanup)..\n")

    print("Checking plant health...")
    gm.check_plant_health()

    print("Testing error recovery...")
    try:
        gm.water_plants(56)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
