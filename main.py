"""Print the first 20 prime numbers to the console."""

from __future__ import annotations


def _is_prime(n: int) -> bool:
    """Return True if ``n`` is a prime number, otherwise False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def main() -> None:
    """Print the first 20 prime numbers, one per line, to stdout."""
    count = 0
    candidate = 2

    while count < 20:
        if _is_prime(candidate):
            print(candidate)
            count += 1
        candidate += 1


if __name__ == "__main__":
    main()
