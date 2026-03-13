#!/usr/bin/env python3

class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system..")
    plants = ["tomato", "lettuce", "carrot"]
    try:
        for x in plant_list:
            if x not in plants:
                raise InvalidPlant(f"Cannot water {x} - invalid plant!")
            print(f"Watering {x} - success")
    except InvalidPlant as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)..")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    plant_list1 = ["tomato", "lettuce", "carrot"]
    plant_list2 = ["tomato", "truck", "carrot"]
    try:
        print("Testing normal watering...")
        water_plants(plant_list1)
        print("Watering completed successfully!")
        print("\nTesting with error...")
        water_plants(plant_list2)
    except InvalidPlant as e:
        print(f"Error: {e}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
