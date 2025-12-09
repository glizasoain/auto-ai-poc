from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import main


def test_main_prints_first_20_primes_to_stdout() -> None:
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
    expected_lines = [str(p) for p in expected_primes]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
