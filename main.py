"""Print the first 20 prime numbers to the console."""

from __future__ import annotations


def print_range(start: int, end: int) -> None:
    """Print integers from `start` to `end` inclusive, one per line."""
    for number in range(start, end + 1):
        print(number)


def _is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    limit = int(n**0.5) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return False
    return True


def _generate_first_n_primes(n: int) -> list[int]:
    """Generate a list containing the first `n` prime numbers."""
    primes: list[int] = []
    candidate = 2
    while len(primes) < n:
        if _is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def main() -> None:
    """Print the first 20 prime numbers, one per line, to stdout."""
    for prime in _generate_first_n_primes(20):
        print(prime)


if __name__ == "__main__":
    main()
