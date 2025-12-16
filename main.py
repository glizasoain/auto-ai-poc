"""Print the first 20 prime numbers to the console."""

from __future__ import annotations


def _is_prime(n: int) -> bool:
    """Return True if `n` is a prime number, otherwise False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n**0.5) + 1
    for factor in range(3, limit, 2):
        if n % factor == 0:
            return False
    return True


def main() -> None:
    """Print the first 20 prime numbers, one per line, to stdout."""
    primes: list[int] = []
    candidate = 2

    while len(primes) < 20:
        if _is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    for prime in primes:
        print(prime)


if __name__ == "__main__":
    main()
