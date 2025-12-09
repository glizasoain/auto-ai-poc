from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import pytest

import main


def test_first_n_primes_exists_on_main_module() -> None:
    """Ensure prime utilities are present on main.py as part of GUIL-29."""
    assert hasattr(main, "first_n_primes")
    assert callable(main.first_n_primes)


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, []),
        (1, [2]),
        (2, [2, 3]),
        (5, [2, 3, 5, 7, 11]),
        (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
    ],
)
def test_first_n_primes_returns_expected_sequence(n: int, expected: list[int]) -> None:
    assert main.first_n_primes(n) == expected


def test_main_prints_first_20_primes_to_stdout() -> None:
    expected_lines = [str(n) for n in main.first_n_primes(20)]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
