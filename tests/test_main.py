from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import main


def test_first_n_primes_returns_first_10_primes() -> None:
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert main.first_n_primes(10) == expected


def test_main_prints_numbers_101_to_120_to_stdout() -> None:
    expected_lines = [str(n) for n in range(101, 121)]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
