from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import pytest

import main


def test_first_n_primes_exists_and_returns_correct_first_20_primes() -> None:
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


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, []),
        (1, [2]),
        (2, [2, 3]),
        (5, [2, 3, 5, 7, 11]),
    ],
)
def test_first_n_primes_various_counts(n: int, expected: list[int]) -> None:
    assert main.first_n_primes(n) == expected


def test_is_prime_basic_cases() -> None:
    assert not main.is_prime(0)
    assert not main.is_prime(1)
    assert main.is_prime(2)
    assert main.is_prime(3)
    assert not main.is_prime(4)
    assert main.is_prime(5)
    assert not main.is_prime(9)
    assert main.is_prime(11)


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
