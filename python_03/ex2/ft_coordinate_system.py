#!/usr/bin/env python3
import sys
import math


def calc_distance(b: tuple, e: tuple) -> float:
    return math.sqrt((e[0]-b[0])**2 + (e[1]-b[1])**2 + (e[2]-b[2])**2)


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    spawn = (10, 20, 5)
    zero = (0, 0, 0)
    distance = calc_distance(zero, spawn)
    print(f"Position created: {spawn}")
    print(f"Distance between {zero} and {spawn}: {distance:.2f}\n")

    try:
        print(f'Parsing coordinates: "{sys.argv[1]}"')
        tmp_tpl = sys.argv[1].split(",")
        tmp_lst = []
        for x in tmp_tpl:
            try:
                tmp_lst.append(int(x))
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - Type: ValueError, Args: {e.args}\n")
        player = tuple(tmp_lst)
        print(f"Parsed positions: {player}")
        distance = calc_distance(zero, player)
        print(f"Distance between {zero} and {player}: {distance:.1f}\n")
    except IndexError:
        print("Invalid arguments.")
        return
    print('Parsing invalid coordinates: "abc,def,ghi"')
    tmp_tpl = ("abc", "def", "ghi")
    tmp_lst = []
    try:
        tmp_lst.append(int(tmp_tpl[0]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")
    print("Unpacking demonstration:")
    x, y, z = player
    print(f"Player at x={player[0]}, y={player[1]}, z={player[2]}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
