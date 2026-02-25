#!/usr/bin/env python3
import sys


def ft_score_analytics() -> None:
    """Processes player scores from the command line to generate analytics."""
    print("=== Player Score Analytics ===\n")
    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage : python3 ft_score_analytics.py "
            "<score1> <score2>..."
            )
    else:
        scores = []
        print("Processing scores...")
        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError:
                print(f"Nuh uh, {arg} is not a number!")
        quantity_s = len(scores)
        total_s = sum(scores)
        max_s = max(scores)
        min_s = min(scores)
        average_s = total_s / quantity_s
        range_s = max_s - min_s
        print(f"\nScores processed: {scores}")
        print(f"Total players: {quantity_s}")
        print(f"Total score: {total_s}")
        print(f"Average score: {average_s:.1f}")
        print(f"Highest score: {max_s}")
        print(f"Lowest score: {min_s}")
        print(f"Score range: {range_s}")


if __name__ == "__main__":
    ft_score_analytics()
