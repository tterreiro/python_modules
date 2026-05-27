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
    fire_enchantment = partial(base_enchantment, 50, "Fire")
    ice_enchantment = partial(base_enchantment, 50, "Ice")
    earth_enchantment = partial(base_enchantment, 50, "Earth")
    enchantments = {"fire": fire_enchantment,
                    "ice": ice_enchantment,
                    "earth": earth_enchantment}
    return enchantments


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-3)


def spell_dispatcher() -> Callable[[Any], str]:
    pass


if __name__ == "__main__":
    pass