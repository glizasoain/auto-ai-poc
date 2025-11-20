# simple-number-demo

This repository now holds a very small Python program for experimentation with autonomous agents. It prints the numbers 201 through 220 to standard output.

## Requirements
- Python 3.9+ (comes with macOS 14+ by default)

## Usage
From the project root, run:

```bash
python main.py
```

You should see the numbers 201, 202, ..., 220 each on their own line.

## Implementation details

- `main.py`
  - `main()` prints the integers from 201 to 220 inclusive, one per line, to stdout.
  - `print_range(start, end)` is a small helper that prints any inclusive integer range.
  - `is_prime(n)` and `first_n_primes(count)` are utility functions used for testing and experimentation.

- `tests/test_main.py`
  - Verifies that `first_n_primes(10)` returns the first 10 prime numbers.
  - Verifies that `main.main()` prints exactly the numbers 201–220, one per line, to stdout.

## Next steps
- Use this minimal script as a sandbox for evaluating autonomous coding agents.
- Extend `main.py` however you like; it currently has no dependencies or frameworks to get in the way.
