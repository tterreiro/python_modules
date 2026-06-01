#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {"add": add,
                  "multiply": mul,
                  "max": max,
                  "min": min}
    if not spells:
        return 0
    if operation not in operations.keys():
        raise ValueError("Unkown operation.")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchantment = partial(base_enchantment, 50, "fire")
    ice_enchantment = partial(base_enchantment, 50, "ice")
    earth_enchantment = partial(base_enchantment, 50, "earth")
    enchantments = {"fire": fire_enchantment,
                    "ice": ice_enchantment,
                    "earth": earth_enchantment}
    return enchantments


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 2 or n == 1:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell_handler(spell: Any) -> str:
        return "Unkown spell type"

    @spell_handler.register(list)
    def _1(spell: list) -> str:
        return f"{len(spell)} spells"

    @spell_handler.register(str)
    def _2(spell: str) -> str:
        return f"{spell}"

    @spell_handler.register(int)
    def _3(spell: int) -> str:
        return f"{spell} damage"
    return spell_handler


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells = [24, 53, 52]
    try:
        print(f"Sum: {spell_reducer(spells, "add")}")
        print(f"Product: {spell_reducer(spells, "multiply")}")
        print(f"Max: {spell_reducer(spells, "max")}")
        print(spell_reducer(spells, "Quadruplicate"))
    except Exception as e:
        print(e)
    print("\nTesting partial enchanter...")

    def base_enchantment(power: str, element: str, target: str) -> str:
        return f"{target} got hit with {element} ball for {power} damage"
    ele_enchants = partial_enchanter(base_enchantment)
    print(
        f"Fire enchant: {ele_enchants['fire']('John pork')}\n"
        f"Ice enchant: {ele_enchants['ice']('John pork')}\n"
        f"Earth enchant: {ele_enchants['earth']('John pork')}")

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher(['spell1', 'spell2', 'spell3'])}")
    print(f"{dispatcher({'john': 'pork'})}")
