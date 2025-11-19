"""Print the numbers from 101 to 120 to the console.

The numbers printed are:
101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
111, 112, 113, 114, 115, 116, 117, 118, 119, 120
"""

from __future__ import annotations


def numbers_from_101_to_120() -> list[int]:
    """Return a list of the integers from 101 through 120 inclusive."""
    return list(range(101, 121))


def main() -> None:
    """Print the numbers from 101 to 120, one per line, to stdout, in ascending order."""
    for number in numbers_from_101_to_120():
        print(number)


if __name__ == "__main__":
    main()
