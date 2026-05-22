#!/usr/bin/env python3
from collections.abc import Callable


def mage_counter() -> Callable:
    i = 0

    def call_counter() -> int:
        nonlocal i
        i += 1
        return i
    return call_counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def increase_power(amount) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return increase_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value: str) -> None:
        nonlocal storage
        storage.update({key: value})

    def recall(key: str) -> str:
        if key in storage.keys():
            return storage.get(key) if True else return "lalal"
        else:
            return "Memory not found"

