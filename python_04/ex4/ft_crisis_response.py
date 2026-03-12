#!/usr/bin/env python3


def ft_crisis_response(file: str) -> None:
    try:
        with open(file, "r") as archive:
            print(f"\nROUTINE ACCESS: Attempting access to '{file}'...")
            print(f'SUCCESS: Archive recovered - "{archive.read()}"')
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    ft_crisis_response("lost_archive.txt")
    ft_crisis_response("classified_vault.txt")
    ft_crisis_response("standard_archive.txt")
    print("\nAll crisis scenarios handled successfully. Archives secure.")
