from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import main


def test_first_n_primes_returns_first_10_primes() -> None:
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert main.first_n_primes(10) == expected


def test_main_prints_first_10_primes_to_stdout() -> None:
    expected_lines = ["29", "23", "19", "17", "13", "11", "7", "5", "3", "2"]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
