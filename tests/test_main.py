from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import pytest

import main


def test_is_prime_basic_cases() -> None:
    assert main.is_prime(0) is False
    assert main.is_prime(1) is False
    assert main.is_prime(2) is True
    assert main.is_prime(3) is True
    assert main.is_prime(4) is False
    assert main.is_prime(17) is True
    assert main.is_prime(18) is False


def test_first_n_primes_returns_correct_sequence() -> None:
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    assert main.first_n_primes(20) == expected


def test_main_prints_first_20_primes_to_stdout() -> None:
    expected_lines = [str(n) for n in main.first_n_primes(20)]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
