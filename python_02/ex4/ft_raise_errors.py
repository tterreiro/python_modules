#!/usr/bin/env python3


def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
        ) -> str:
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Sun hours {sunlight_hours} is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing with good values...")
    try:
        print(check_plant_health("Tomato", 5, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 5, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("Tomato", 15, 5))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("Tomato", 5, 0))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error relating tests completed!")


if __name__ == "__main__":
    test_plant_checks()
