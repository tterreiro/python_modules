#!/usr/bin/env python3
import alchemy.grimoire


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimore module directly")
    igr = "Earth wind and FirE"
    print("Testing record light spell:",
          alchemy.grimoire.light_spell_record("Fantasy", igr))
