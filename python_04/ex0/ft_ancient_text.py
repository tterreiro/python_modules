#!/usr/bin/env python3

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = None
    try:
        file = open("ancient_fragment.txt")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())
    except OSError:
        print("ERROR: Storage vault not found.\n")
    if file:
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
