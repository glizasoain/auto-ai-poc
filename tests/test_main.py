from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import pytest

import main


def test_first_n_primes_exists_and_returns_correct_first_5_primes() -> None:
    """Ensure first_n_primes is available and returns the expected primes."""
    assert hasattr(main, "first_n_primes")

    result = main.first_n_primes(5)
    assert result == [2, 3, 5, 7, 11]


def test_first_n_primes_returns_first_20_primes() -> None:
    expected_first_20 = [
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

    result = main.first_n_primes(20)
    assert result == expected_first_20


def test_main_prints_first_20_primes_to_stdout() -> None:
    expected_lines = [
        "2",
        "3",
        "5",
        "7",
        "11",
        "13",
        "17",
        "19",
        "23",
        "29",
        "31",
        "37",
        "41",
        "43",
        "47",
        "53",
        "59",
        "61",
        "67",
        "71",
    ]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
