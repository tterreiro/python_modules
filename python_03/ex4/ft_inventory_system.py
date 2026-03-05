#!/usr/bin/env python3
import sys


def inv_parse() -> dict:
    """Parses command-line arguments into an inventory dictionary."""
    inventory = {}
    for item in sys.argv[1:]:
        tmp = item.split(":")
        try:
            tmp[1] = int(tmp[1])
            if tmp[1] < 1:
                raise ValueError
            inventory.update(dict([tmp]))
        except (ValueError, IndexError):
            print(f"This aint right, son. (by this I mean {item})")
    return inventory


def ft_inventory_system() -> None:
    """Analyzes game inventory and generates a status report."""
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")
        inventory = inv_parse()
        item_amnt = 0
        for x in inventory.values():
            item_amnt += x
        print(f"Total items in inventory: {item_amnt}")
        print(f"Unique items types: {len(inventory)}\n")

        print("=== Current Inventory ===")
        most = None
        least = None
        moderate = {}
        scarce = {}
        restock = []
        for item, value in inventory.items():
            if most is None or value > inventory[most]:
                most = item
            if least is None or value < inventory[least]:
                least = item
            if value >= 5:
                moderate.update({item: value})
            else:
                if value < 2:
                    restock.append(item)
                scarce.update({item: value})
            percentage = (value / item_amnt) * 100
            print(
                f"{item}: {value} units ({percentage:.1f}%)")

        print("\n=== Inventory Statistics ===")
        print(f"Most abundant: {most} ({inventory[most]} units)")
        print(f"Least abundant: {least} ({inventory[least]} units)\n")

        print("=== Item Categories ===")
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        print("\n=== Management Suggestions ===")
        print(f"Restock needed: {','.join(restock)}\n")

        print("=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {', '.join(inventory.keys())}")
        print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")
        check_item = 'sword'
        print(
            "Sample lookup - "
            f"{check_item} in inventory: {check_item in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
