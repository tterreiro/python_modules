#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        nbr = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number\n")
    if nbr > 40:
        raise ValueError(f"{nbr}°C is too hot for plants (max 40°C)\n")
    elif nbr < 0:
        raise ValueError(f"{nbr}°C is too cold for plants (min 0°C)\n")
    print("Temperature 25°C is perfect for plants!\n")
    return nbr


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    test = ["25", "abc", "100", "-50"]
    for x in test:
        try:
            print(f"Testing temperature: {x}")
            check_temperature(x)
        except ValueError as e:
            print(f"Error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
