#!/usr/bin/env python3


def ft_garden_intro(name: str, height: float, age: int) -> None:
    """
    Prints a welcome message for a specific garden plant.
    """
    print("\n=== Welcome to Jack's garden! ===\n")
    print(f"Plant: {name}\nHeight: ~{height}m\nAge: {age} years")
    print("\n=== End of program ===\n")


if __name__ == "__main__":
    ft_garden_intro("Beanstalk", 2000, 5000)
