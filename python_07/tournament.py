#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory, AquaFactory, FlameFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy)


def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved")
    try:
        for i in range(len(opps)):
            for j in range(i + 1, len(opps)):
                print("\n* Battle *")
                opp_a, strategy_a = opps[i]
                opp_b, strategy_b = opps[j]
                creature_a = opp_a.create_base()
                creature_b = opp_b.create_base()
                print(
                    f"{creature_a.describe()}\n"
                    " vs.\n"
                    f"{creature_b.describe()}\n"
                    " now fight!"
                )
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
    except Exception as e:
        print(f"Battle Error, aborting tournament: {e}")


if __name__ == "__main__":
    print("Tournament 0 (basics)")
    t_0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(t_0)
    t_1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Agressive), (Healing+Defensive) ]")
    battle(t_1)
    t_2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(t_2)
