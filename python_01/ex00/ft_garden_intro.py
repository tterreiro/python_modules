#!/usr/bin/env python3


def ft_garden_intro(name: str, height: float, age: int) -> None:
    """
    Prints a welcome message for a specific garden plant.

    Args:
        name (str): The name of the plant.
        height (int): Height in meters.
        age (int): Age in years.
    """
    print("\n=== Welcome to my fucking garden, HELL YEAH! ===\n")
    print(f"Plant: {name}\nHeight: ~{height}m\nAge: {age} years")
    print("\n=== Hope you liked my garden :) ===\n")


if __name__ == "__main__":
    ft_garden_intro("Beanstalk", 2000, 5000)
