def generate_first_n_primes(count: int) -> list[int]:
    ...

def main() -> None:
    """Print the first 20 prime numbers, one per line, to stdout."""
    for prime in generate_first_n_primes(20):
        print(prime)
