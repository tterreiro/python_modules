#!/usr/bin/env python3
import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(
        f"{base.describe()}\n"
        f"{base.attack()}\n"
        f"{evolved.describe()}\n"
        f"{evolved.attack()}\n"
    )


def ft_battle(flame_fac: ex0.FlameFactory, water_fac: ex0.AquaFactory) -> None:
    print("Testing battle")
    flameling = flame_fac.create_base()
    aquabub = water_fac.create_base()
    print(
        f"{flameling.describe()}\n"
        " vs\n"
        f"{aquabub.describe()}\n"
        " fight!\n"
        f"{flameling.attack()}\n"
        f"{aquabub.attack()}\n"
        )


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    try:
        test_factory(flame_factory)
        test_factory(aqua_factory)
        ft_battle(flame_factory, aqua_factory)
    except Exception as e:
        print(f"Error: {e}")
