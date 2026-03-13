#!/usr/bin/env python3
import sys


def inv_parse() -> dict:
    inventory = {}
    for item in sys.argv[1:]:
        tmp = item.split(":")
        try:
            tmp[1] = int(tmp[1])
            if tmp[1] < 1:
                raise ValueError
            inventory.update(dict([tmp]))
        except (ValueError, IndexError, KeyError) as e:
            raise e.__class__(f"This aint right, son. (by this I mean {item})")
    return inventory


def ft_inventory_system() -> None:
    if len(sys.argv) > 1:
        print("=== Inventory System Analysis ===")
        try:
            inventory = inv_parse()
        except (ValueError, IndexError, KeyError) as e:
            print(e)
            exit(1)
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
        print("Restock needed: ", end='')
        print(*restock, sep=', ')

        print("=== Dictionary Properties Demo ===")
        print("Dictionary keys: ", end='')
        print(*inventory.keys(), sep=', ')
        print("Dictionary values: ", end='')
        print(*inventory.values(), sep=", ")
        check_item = 'sword'
        print(
            "Sample lookup - "
            f"{check_item} in inventory: {check_item in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
