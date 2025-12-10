import io
from contextlib import redirect_stdout

import pytest

import main


def test_is_prime_basic_cases():
    # Non-primes
    assert main.is_prime(-10) is False
    assert main.is_prime(0) is False
    assert main.is_prime(1) is False
    assert main.is_prime(4) is False
    assert main.is_prime(9) is False
    assert main.is_prime(21) is False

    # Primes
    assert main.is_prime(2) is True
    assert main.is_prime(3) is True
    assert main.is_prime(5) is True
    assert main.is_prime(7) is True
    assert main.is_prime(19) is True
    assert main.is_prime(97) is True


def test_first_n_primes_returns_correct_sequence():
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
    assert main.first_n_primes(20) == expected_first_20


def test_first_n_primes_zero_count():
    assert main.first_n_primes(0) == []


def test_first_n_primes_raises_for_negative_count():
    with pytest.raises(ValueError):
        main.first_n_primes(-1)


def test_main_prints_first_20_primes_to_stdout():
    buf = io.StringIO()
    with redirect_stdout(buf):
        main.main()
    output = buf.getvalue().strip().splitlines()

    expected_first_20 = [
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

    assert output == expected_first_20
