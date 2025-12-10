"""Print the first 20 prime numbers to the console."""

from __future__ import annotations

from primes import first_n_primes


def main() -> None:
    """Print the first 20 prime numbers, one per line, to stdout."""
    for prime in first_n_primes(20):
        print(prime)


if __name__ == "__main__":
    main()
