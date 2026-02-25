#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Validates temperature input using exceptions"""
    try:
        nbr = int(temp_str)
        if nbr > 40:
            print(f"Error: {nbr}°C is too hot to handle (max 40°C)\n")
            return None
        elif nbr < 0:
            print(f"Error: {nbr}°C is too cold for plants (min 0°C)\n")
            return None
        else:
            return nbr
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    """Tests the function"""
    print("=== Garden Temperature Checker ===\n")
    test = ["25", "abc", "100", "-50"]
    for x in test:
        print(f"Testing temperature: {x}")
        check = check_temperature(x)
        if check is not None:
            print(f"Temperature {check}°C is perfect for plants!\n")
    print("All tests completed - program didnt crash!")


if __name__ == "__main__":
    test_temperature_input()
