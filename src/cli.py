"""Command-line interface that renders a filled circle image."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Optional

from .draw import draw_circle

DEFAULT_OUTPUT = Path("artifacts/circle.png")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render a filled circle image.")
    parser.add_argument(
        "--radius",
        type=float,
        default=100.0,
        help="Circle radius in pixels (default: 100)",
    )
    parser.add_argument(
        "--color",
        type=str,
        default="#228be6",
        help="Fill color in hex format (default: #228be6)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Path to save the circle image (default: {DEFAULT_OUTPUT})",
    )
    return parser


def main(argv: Optional[Iterable[str]] = None) -> Path:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    image_path = draw_circle(args.radius, args.color, args.output)
    print(f"Saved circle image to {image_path}")
    return image_path


if __name__ == "__main__":  # pragma: no cover
    main()
