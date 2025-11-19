from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

import main


def test_numbers_from_101_to_120_returns_correct_sequence() -> None:
    expected = list(range(101, 121))
    assert main.numbers_from_101_to_120() == expected


def test_main_prints_numbers_from_101_to_120_to_stdout() -> None:
    expected_lines = [str(n) for n in range(101, 121)]

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.main()

    output = buffer.getvalue().strip().splitlines()
    assert output == expected_lines
