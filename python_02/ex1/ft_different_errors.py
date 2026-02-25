#!/usr/bin/env python3

def garden_operations(error_type: str) -> None:
    """Tests various types of errors"""
    if error_type.upper() == "VALUEERROR":
        try:
            int("abc")
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
    elif error_type.upper() == "ZERODIVISIONERROR":
        try:
            4 / 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
    elif error_type.upper() == "FILENOTFOUNDERROR":
        try:
            open("wobblygrobble.txt")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    elif error_type.upper() == "KEYERROR":
        try:
            dic = {"brutal": "compal"}
            print(dic["brigitte"])
        except KeyError:
            print("Caught KeyError: missing 'brigitte'\n")
    elif error_type == "Multiple errors together":
        try:
            4 / 0
        except (ZeroDivisionError, ValueError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """Tests function"""
    print("=== Garden Error Types Demo ===\n")
    test = [
        "ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError",
        "Multiple errors together"]
    for x in test:
        print(f"Testing {x}...")
        garden_operations(x)
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
