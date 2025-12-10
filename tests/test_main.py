## Summary

This PR addresses [GUIL-31](https://your-jira-url/browse/GUIL-31) by confirming and codifying the behavior of the CLI script to print the first 20 prime numbers.

## Changes

- Verified `main.main()` prints the first 20 prime numbers, one per line, to stdout.
- Confirmed `first_n_primes(count)` returns the correct sequence of primes.
- Confirmed `is_prime(n)` correctly identifies prime vs non-prime integers for a representative set of inputs.
- Ensured tests cover:
  - Prime generation (`first_n_primes`)
  - Primality checking (`is_prime`)
  - End-to-end output of the script (`main.main`)

## Testing

- Ran `pytest` and confirmed all tests pass.

## Jira

- Resolves [GUIL-31](https://your-jira-url/browse/GUIL-31)
- Branch: `ai/GUIL-31/change-the-existing-code-to-print-the-fi-d2e697`
