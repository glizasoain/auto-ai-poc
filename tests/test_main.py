from __future__ import annotations

from io import StringIO
from contextlib import redirect_stdout

import builtins

import main


def test_main_prints_first_20_primes_to_stdout() -> None:
    """main() should print the first 20 prime numbers, one per line."""
    expected_primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
    ]
    expected_output = "\n".join(str(p) for p in expected_primes) + "\n"

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    assert buffer.getvalue() == expected_output


def test_is_prime_basic_cases() -> None:
    """Sanity-check _is_prime on a few known values."""
    assert main._is_prime(2) is True
    assert main._is_prime(3) is True
    assert main._is_prime(4) is False
    assert main._is_prime(17) is True
    assert main._is_prime(1) is False
    assert main._is_prime(0) is False
    assert main._is_prime(-5) is False


def test_generate_first_n_primes_returns_correct_list() -> None:
    """_generate_first_n_primes should return the first N primes."""
    assert main._generate_first_n_primes(5) == [2, 3, 5, 7, 11]
    assert main._generate_first_n_primes(1) == [2]
    assert main._generate_first_n_primes(0) == []
