"""Print the first 20 prime numbers to the console."""

from collections.abc import Iterator


def is_prime(n: int) -> bool:
    """Return True if `n` is a prime number, otherwise False.

    Assumes n is a non-negative integer.
    """
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


def first_n_primes(count: int) -> list[int]:
    """Return a list containing the first `count` prime numbers."""
    primes: list[int] = []
    candidate = 2

    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1

    return primes


def iter_first_n_primes(count: int) -> Iterator[int]:
    """Yield the first `count` prime numbers, one at a time."""
    for prime in first_n_primes(count):
        yield prime


def main() -> None:
    """Print the first 20 prime numbers, one per line, to stdout."""
    for prime in iter_first_n_primes(20):
        print(prime)


if __name__ == "__main__":
    main()
