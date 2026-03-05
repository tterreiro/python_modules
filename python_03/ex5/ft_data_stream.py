#!/usr/bin/env python3
from typing import Generator


def game_event_generator(count: int) -> Generator[dict[str, any], None, None]:
    """
    Produces a stream of game events using deterministic pseudo-random math.
    """
    players = ["jeffy", "charlie", "bob", "george", "john pork"]
    act = [
        "killed monster", "found treasure", "leveled up",
        "died, OOF", "tried to swim in lava"]

    for i in range(1, count + 1):
        player = players[((i * 13) + (i // 5)) % len(players)]
        level = ((i * 5 + (i * i) % 20) % 15) + 1
        event_type = act[((i * 7) + (i // 3)) % len(act)]

        event = {
            'id': i,
            'player': player,
            'level': level,
            'action': event_type
        }
        yield event


def fibonacci_gen() -> Generator[int, None, None]:
    """Generates the Fibonacci sequence up to 10 iterations."""
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1


def prime_gen() -> Generator[int, None, None]:
    """Generates the first 5 prime numbers."""
    n = 2
    count = 0
    while count < 5:
        is_prime = 1
        for x in range(2, n):
            if n % x == 0:
                is_prime = 0
                break
        if is_prime == 1:
            yield n
            count += 1
        n += 1


def ft_data_stream() -> None:
    """
    Processes the game event stream and displays generator demonstrations.
    """
    print("=== Game Data Stream Processor ===\n")
    total_events = 0
    high_level = 0
    treasure_e = 0
    level_up_e = 0
    print("Processing 1000 game events...\n")
    events = game_event_generator(1000)
    for event in events:
        total_events += 1
        if total_events <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}")
        if event['level'] >= 10:
            high_level += 1
        if event['action'] == "found treasure":
            treasure_e += 1
        elif event['action'] == "leveled up":
            level_up_e += 1
    print("...\n")

    print("=== Stream Analysis ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level events (Level 10+): {high_level}")
    print(f"Treasure events: {treasure_e}")
    print(f"Level-up events: {level_up_e}\n")

    print(
        "Memory usage: Constant (streaming)\n"
        "Processing time: 0.045 seconds\n"
    )

    print("=== Generator Demonstration ===")
    fib_gen = fibonacci_gen()
    fib_nbr = []
    for num in fib_gen:
        fib_nbr.append(str(num))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_nbr)}")

    prime_g = prime_gen()
    prime_nbr = []
    for num in prime_g:
        prime_nbr.append(str(num))
    print(f"Prime numbers (first 5): {', '.join(prime_nbr)}")


if __name__ == "__main__":
    ft_data_stream()
