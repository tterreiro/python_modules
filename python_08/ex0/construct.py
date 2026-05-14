#!/usr/bin/env python3
import sys
import os
import site


def outside_matrix() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print(
        "WARNING: You're in the global environment!"
        "The machines can see everything you install.\n")
    print(
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n"
        "\nThen run this program again.")


def inside_matrix() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print(
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n")
    print(
        f"Package installation path:\n {site.getsitepackages()[0]}")


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        outside_matrix()
    else:
        inside_matrix()
