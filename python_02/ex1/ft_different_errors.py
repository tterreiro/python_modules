#!/usr/bin/env python3

def garden_operations(error_type: str) -> None:
    if error_type == "ValueError":
        try:
            int("abc")
        except ValueError:
            raise ValueError("ValueError: invalid literal for int()")
    elif error_type == "ZeroDivisionError":
        try:
            4 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("ZeroDivisionError: division by zero")
    elif error_type == "FileNotFoundError":
        try:
            open("wobblygrobble.txt")
        except FileNotFoundError:
            raise FileNotFoundError(
                "FileNotFoundError: No such file 'missing.txt'")
    elif error_type == "KeyError":
        try:
            dic = {"brutal": "compal"}
            print(dic["brigitte"])
        except KeyError as e:
            raise KeyError(f"KeyError: {e}")
    elif error_type == "Multiple errors together":
        try:
            4 / 0
            open("wobblygrobble.txt")
            int("abc")
        except (ZeroDivisionError, ValueError,
                FileNotFoundError, KeyError) as e:
            raise e.__class__("an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    test = [
        "ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError",
        "Multiple errors together"]
    for x in test:
        print(f"Testing {x}...")
        try:
            garden_operations(x)
        except (ZeroDivisionError, ValueError,
                FileNotFoundError, KeyError) as e:
            print(f"Caught {e}\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
