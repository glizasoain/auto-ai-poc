# simple-number-demo

This repository now holds a very small Python program for experimentation with autonomous agents. It prints the first 20 prime numbers to standard output.

## Requirements
- Python 3.9+ (comes with macOS 14+ by default)

## Usage
From the project root, run:

```bash
python main.py
```

You should see the first 20 prime numbers, each on their own line:

```text
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
```

## Implementation details

- `main.py`
  - `main()` prints the first 20 prime numbers, one per line, to stdout.
  - `_is_prime(n)` is a small helper that returns `True` if `n` is prime, otherwise `False`.
  - `_generate_first_n_primes(count)` returns a list containing the first `count` prime numbers.

- `tests/test_main.py`
  - Verifies that `main.main()` prints exactly the first 20 prime numbers, one per line, to stdout.
  - Sanity-checks `_is_prime` on a few known values.
  - Verifies that `_generate_first_n_primes(count)` returns the correct list of primes for several small counts.

## Next steps
- Use this minimal script as a sandbox for evaluating autonomous coding agents.
- Extend `main.py` however you like; it currently has no dependencies or frameworks to get in the way.
