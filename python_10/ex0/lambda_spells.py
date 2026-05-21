#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mages: mages['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spells: '* ' + spells + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    mx_power = max(map(lambda mages: mages['power'], mages))
    min_power = min(map(lambda mages: mages['power'], mages))
    avg_power = (
        round(sum(map(lambda mages: mages['power'], mages)) / len(mages), 2))
    return (
        {'max_power': mx_power, 'min_power': min_power, "avg_power": avg_power}
        )


if __name__ == "__main__":
    artifacts = [{'name': 'Shadow Blade', 'power': 101, 'type': 'focus'},
                 {'name': 'Lightning Rod', 'power': 83, 'type': 'relic'},
                 {'name': 'Storm Crown', 'power': 62, 'type': 'relic'},
                 {'name': 'Light Prism', 'power': 117, 'type': 'relic'}]
    mages = [{'name': 'Nova', 'power': 74, 'element': 'fire'},
             {'name': 'Ash', 'power': 62, 'element': 'shadow'},
             {'name': 'Alex', 'power': 67, 'element': 'earth'},
             {'name': 'Ash', 'power': 57, 'element': 'earth'},
             {'name': 'Luna', 'power': 93, 'element': 'water'}]
    spells = ['freeze', 'flash', 'shield', 'tsunami']
    print("\nTesting artifact sorter...")
    sorted_art = artifact_sorter(artifacts)
    print(f"{sorted_art[0]["name"]}({sorted_art[0]['power']} power)"
          "comes before"
          f"{sorted_art[1]["name"]}({sorted_art[1]['power']} power)")
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print("\nTesting power filter...")
    min_power = 67
    valid_mages = power_filter(mages, min_power)
    print(f"Mages with mininimum power of {min_power}:")
    for mage in valid_mages:
        print(f"{mage['name']} ({mage['power']} power)")
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    for stat, val in stats.items():
        print(f"{stat}: {val}")
