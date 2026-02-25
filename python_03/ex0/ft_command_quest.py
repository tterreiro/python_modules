#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    """Parses and displays command-line arguments."""
    print("=== Command Quest ===")
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
