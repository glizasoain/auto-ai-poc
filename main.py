"""Print the numbers from 2201 to 2220 in reverse order to the console."""

def print_range(start: int, end: int) -> None:
    """Print integers from `start` to `end` inclusive, one per line."""
    for number in range(start, end + 1):
        print(number)


def main() -> None:
    """Print the numbers from 2201 to 2220 in reverse order, one per line, to stdout."""
    for number in range(2220, 2200, -1):
        print(number)


if __name__ == "__main__":
    main()
