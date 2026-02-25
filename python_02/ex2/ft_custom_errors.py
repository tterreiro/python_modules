#!/usr/bin/env python3

class GardenError(Exception):
    """Garden error"""
    pass


class PlantError(GardenError):
    """Plant error"""
    pass


class WaterError(GardenError):
    """Water error"""
    pass


def test_error() -> None:
    """Tests custom exception"""
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    status = "wilting"
    try:
        if (status == "wilting"):
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    else:
        print(f"Tomato is {status}, looks ok.")

    print("\nTesting WaterError...")
    watering_tank = 4
    try:
        if (watering_tank < 20):
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError : {e}")
    else:
        print(f"Water tank have {watering_tank}L of water, looks ok.")

    print("\nTesting catching all garden errors...")
    try:
        if (status == "wilting"):
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    else:
        print(f"Tomato plant is {status}, seem's fine.")
    try:
        if (watering_tank < 20):
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    else:
        print(f"Water tank have {watering_tank}L of water, seem's enough.")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error()
