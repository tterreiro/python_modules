#!/usr/bin/env python3
from collections.abc import Callable


def necrosis(target: str, power: int) -> str:
    return f"Necrosis took over {target} for {power} DMG"


def fireball(target: str, power: int) -> str:
    return f"{target} got hit by a Fireball for {power} DMG"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def checker(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell Fizzled"
    return checker


def spell_sequence(spells: list[Callable]) -> Callable:
    def iterator(target: str, power: int) -> list[str]:
        spell_results = []
        for spell in spells:
            spell_results.append(spell(target, power))
        return spell_results
    return iterator


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combiner = spell_combiner(necrosis, fireball)
    if callable(combiner):
        print("Combined spell result:", ", ".join(combiner('Netanyahu', 67)))
    print("\nTesting spell amplifier...")
    amplifier = power_amplifier(fireball, 3)
    power = 33
    if callable(amplifier):
        print(
            f"Original: {power}, Amplified: {amplifier('Charlie kirk', power)}"
            )
    print("\nTesting spell caster...")
    caster = conditional_caster(
        lambda target, power: target != "Triple T" and power > 15, necrosis)
    if callable(caster):
        print(f"Follows condition: {caster('Sponge bob', 9817498172)}"
              f"\nDoesn't follow condition: {caster('Charlie kirk', 1)}")
    print("\nTesting spell sequence...")
    iterator = spell_sequence([fireball, necrosis])
    if callable(iterator):
        print(f"Spell sequence: {', '.join(iterator('John pork', 24))}")
