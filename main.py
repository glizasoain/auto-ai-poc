"""Print the numbers from 201 to 220 to the console."""

def print_range(start: int, end: int) -> None:
    """Print integers from `start` to `end` inclusive, one per line."""
    for number in range(start, end + 1):
        print(number)


def main() -> None:
    """Print the numbers from 201 to 220, one per line, to stdout."""
    print_range(201, 220)


if __name__ == "__main__":
    main()
