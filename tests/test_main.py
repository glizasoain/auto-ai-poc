from __future__ import annotations

from io import StringIO
from typing import List
from unittest import mock

import builtins
import importlib
import types


def run_main_and_capture_output() -> List[str]:
    """Import main module, run main(), and capture printed lines."""
    # Import lazily inside the function so tests don't run on import
    import main  # type: ignore

    # Reload in case of stateful changes between tests
    importlib.reload(main)

    output = StringIO()
    with mock.patch.object(builtins, "print") as mock_print:
        main.main()  # type: ignore[attr-defined]

    # Collect all positional args passed to print
    lines: List[str] = []
    for call in mock_print.call_args_list:
        args = call.args
        if not args:
            continue
        # Only consider the first positional argument as the printed value
        lines.append(str(args[0]))
    return lines


def test_main_prints_numbers_201_to_220_inclusive() -> None:
    lines = run_main_and_capture_output()

    # Expect exactly 20 lines: 201..220 inclusive
    assert len(lines) == 20, f"Expected 20 lines, got {len(lines)}"

    expected = [str(n) for n in range(201, 221)]
    assert lines == expected
