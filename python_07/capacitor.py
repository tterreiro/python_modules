#!/usr/bin/env python3
import ex1


def healing_test(factory: ex1.HealingCreatureFactory) -> None:
    base = factory.create_base()
    evo = factory.create_evolved()
    print(
        "Testing Creature with healing capability\n"
        " base:\n"
        f"{base.describe()}\n"
        f"{base.attack()}")
    if isinstance(base, ex1.HealCapability):
        print(base.heal("itself"))
    print(
        " evolved:\n"
        f"{evo.describe()}\n"
        f"{evo.attack()}")
    if isinstance(evo, ex1.HealCapability):
        print(evo.heal("itself and others"))


def tranform_test(factory: ex1.TransformCreatureFactory) -> None:
    base = factory.create_base()
    evo = factory.create_evolved()
    print(
        "Testing Creature with transform capability\n"
        " base:\n"
        f"{base.describe()}\n"
        f"{base.attack()}")
    if isinstance(base, ex1.TransformCapability):
        print(base.transform())
    print(base.attack())
    if isinstance(base, ex1.TransformCapability):
        print(base.revert())
    print(
        " evolved:\n"
        f"{evo.describe()}\n"
        f"{evo.attack()}")
    if isinstance(evo, ex1.TransformCapability):
        print(evo.transform())
    print(evo.attack())
    if isinstance(evo, ex1.TransformCapability):
        print(evo.revert())


if __name__ == "__main__":
    heal_factory = ex1.HealingCreatureFactory()
    trans_factory = ex1.TransformCreatureFactory()
    try:
        healing_test(heal_factory)
        print()
        tranform_test(trans_factory)
    except Exception as e:
        print(f"ERROR: {e}")
