from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import pytest

import main


def test_first_n_primes_function_exists_and_returns_correct_primes() -> None:
    """Ensure first_n_primes is available and returns the first 20 primes."""
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

    assert hasattr(main, "first_n_primes")
    assert main.first_n_primes(20) == expected_primes


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (19, True),
        (1, False),
        (0, False),
        (-5, False),
    ],
)
def test_is_prime_behavior(n: int, expected: bool) -> None:
    """Basic behavioral tests for is_prime helper."""
    assert main.is_prime(n) is expected


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
