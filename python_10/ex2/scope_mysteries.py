#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


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

    def store(key: str, value: Any) -> None:
        nonlocal storage
        storage.update({key: value})

    def recall(key: str) -> str:
        if key and key in storage.keys():
            return storage[key]
        else:
            return "Memory not found"
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print("\nTesting enchant factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']('secret', 42)
    print(f"Recall 'secret' = {vault['recall']('secret')}")
    print(f"Recall 'unknown' = {vault['recall']('unknown')}")
