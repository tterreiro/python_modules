#!/usr/bin/env python3

def ft_achievement_tracker() -> None:
    """Tracks and analyzes unique player achievements using set operations."""
    print("=== Achievement Tracker System ===")
    puffy = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    jeffy = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'perfectionist', 'level_10', 'boss_slayer', 'collector'}
    print(f"Player puffy achievements: {puffy}")
    print(f"Player jeffy achievements: {jeffy}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    all_achiv = puffy.union(jeffy).union(charlie)
    common_achiv = puffy.intersection(jeffy).intersection(charlie)
    rare_achiv = puffy.difference(jeffy).difference(charlie)
    print(f"All unique achievements: {all_achiv}")
    print(f"Total unique achievements: {len(all_achiv)}\n")
    print(f"Common to all players: {common_achiv}")
    print(f"Rare achievements (1 player): {rare_achiv}\n")
    print(f"Puffy vs Jeffy common: {puffy.intersection(jeffy)}")
    print(f"Puffy unique: {puffy.difference(jeffy)}")
    print(f"Jeffy unique: {jeffy.difference(puffy)}")


if __name__ == "__main__":
    ft_achievement_tracker()
