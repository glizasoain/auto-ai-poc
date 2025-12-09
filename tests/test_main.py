import io
from contextlib import redirect_stdout

import main


def test_first_n_primes_exists_on_main_module() -> None:
    """Ensure first_n_primes is defined and callable on the main module."""
    assert hasattr(main, "first_n_primes")
    assert callable(main.first_n_primes)


def test_first_n_primes_returns_expected_sequence() -> None:
    """Verify that first_n_primes returns the correct prime sequences."""
    # 0 primes -> empty list
    assert main.first_n_primes(0) == []

    # 1 prime
    assert main.first_n_primes(1) == [2]

    # 2 primes
    assert main.first_n_primes(2) == [2, 3]

    # 5 primes
    assert main.first_n_primes(5) == [2, 3, 5, 7, 11]

    # 10 primes
    assert main.first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_main_prints_first_20_primes_to_stdout() -> None:
    """Ensure main() prints the first 20 primes, one per line, to stdout."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        main.main()

    output = buf.getvalue().strip().splitlines()
    expected_primes = main.first_n_primes(20)

    # Convert printed lines to integers
    printed_primes = [int(line.strip()) for line in output if line.strip()]

    assert printed_primes == expected_primes
