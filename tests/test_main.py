## Summary

This PR addresses [GUIL-29](https://your-jira-url/browse/GUIL-29) by verifying that the existing implementation already prints the first 20 prime numbers as required.

## Details

- `main.py`
  - `first_n_primes(count: int)` correctly generates the first `count` prime numbers.
  - `main()` calls `first_n_primes(20)` and prints each prime on its own line to stdout.

- `tests/test_main.py`
  - Ensures `first_n_primes` exists and is callable.
  - Validates the output of `first_n_primes` for several values of `n` (0, 1, 2, 5, 10).
  - Captures stdout from `main.main()` and asserts that it prints exactly the first 20 primes, one per line.

No code changes were necessary because the current implementation already fulfills the Jira requirement.

## Testing

