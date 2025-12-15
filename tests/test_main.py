from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import pytest

import main


def test_first_n_primes_removed_from_main_module() -> None:
    """Ensure prime utilities were removed from main.py as part of GUIL-21."""
    with pytest.raises(AttributeError):
        getattr(main, "first_n_primes")


def test_generate_first_n_primes_returns_correct_first_10_primes() -> None:
    """Ensure the prime generator returns the expected first primes."""
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert main.generate_first_n_primes(10) == expected


def test_main_prints_first_20_primes_to_stdout() -> None:
    """Ensure main() prints the first 20 prime numbers, one per line."""
    expected_primes = main.generate_first_n_primes(20)
    expected_lines = [str(p) for p in expected_primes]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
