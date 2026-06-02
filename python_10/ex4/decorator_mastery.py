#!/usr/bin/env python3
from functools import wraps
from collections.abc import Callable
import time
from typing import Any


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        time.sleep(0.100)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator_factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator_factory


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying..."
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        return f"{target} got hit by a Fireball for {power} DMG"
    print(f"Result: {fireball("charlie kirk", 60)}\n")
    print("Testing retrying spell...")

    @retry_spell(3)
    def wazza(castable: bool) -> str:
        if castable:
            return "Wazzaaaahhh spell wohoo yey!"
        else:
            raise ValueError()
    print(wazza(False))
    print(wazza(True))

    print("\nTesting MageGuild...")
    mage_guild = MageGuild()
    print("Testing valid name: ", mage_guild.validate_mage_name("john pork"))
    print("Testing invalid name: ", mage_guild.validate_mage_name("123john"))
    print("Testing valid power: ", mage_guild.cast_spell("lightning", 67))
    print("Testing invalid power: ", mage_guild.cast_spell("lightning", 9))
