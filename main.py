"""Print the numbers from 201 to 220 to the console."""

from __future__ import annotations


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise.

    Uses a simple trial-division algorithm sufficient for the small
    numbers required by this script.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**0.5) + 1
    for candidate in range(3, limit, 2):
        if n % candidate == 0:
            return False
    return True


def first_n_primes(count: int) -> list[int]:
    """Return a list containing the first `count` prime numbers."""
    primes: list[int] = []
    candidate = 2

    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    return primes


def print_range(start: int, end: int) -> None:
    """Print integers from `start` to `end` inclusive, one per line."""
    for number in range(start, end + 1):
        print(number)


def main() -> None:
    """Print the numbers from 201 to 220, one per line, to stdout."""
    print_range(201, 220)


if __name__ == "__main__":
    main()
