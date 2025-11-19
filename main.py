"""Print the first 10 prime numbers to the console.

The primes printed are:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
"""

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


def main() -> None:
    """Print the first 10 prime numbers, one per line, to stdout, in descending order."""
    for prime in reversed(first_n_primes(10)):
        print(prime)


if __name__ == "__main__":
    main()
