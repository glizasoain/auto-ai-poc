from __future__ import annotations


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
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
