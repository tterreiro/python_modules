#!/usr/bin/env python3
import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_ID = input("Input Stream active. Enter archivist ID:")
    status_rep = input("Input Stream active. Enter status report:")
    print(
        f"\n[STANDARD] Archive status from {arch_ID}: {status_rep}",
        file=sys.stdout
        )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
        )
    print("[STANDARD] Data transmission complete\n", file=sys.stdout)
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
