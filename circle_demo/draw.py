"""Utility helpers for validating inputs and drawing a filled circle."""
from __future__ import annotations

from pathlib import Path
from typing import Union

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

NumberLike = Union[int, float]


def validate_radius(value: Union[NumberLike, str]) -> float:
    """Return a sanitized radius value or raise ValueError."""
    if isinstance(value, str):
        value = value.strip()
        if not value:
            raise ValueError("radius cannot be empty")
        try:
            numeric = float(value)
        except ValueError as exc:  # pragma: no cover - defensive
            raise ValueError("radius must be numeric") from exc
    elif isinstance(value, (int, float)):
        numeric = float(value)
    else:
        raise ValueError("radius must be a number or numeric string")

    if numeric <= 0:
        raise ValueError("radius must be positive")

    return numeric


def parse_color(color: str) -> str:
    """Validate a hex color string in the form #RRGGBB."""
    if not isinstance(color, str):
        raise ValueError("color must be a string")

    color = color.strip()
    if len(color) != 7 or not color.startswith("#"):
        raise ValueError("color must be in #RRGGBB format")

    hex_digits = color[1:]
    if not all(ch in "0123456789abcdefABCDEF" for ch in hex_digits):
        raise ValueError("color must contain valid hex digits")

    return "#" + hex_digits.lower()


def draw_circle(radius: Union[NumberLike, str], color: str, output_path: Union[str, Path]) -> Path:
    """Render a filled circle with matplotlib and save it to output_path."""
    sanitized_radius = validate_radius(radius)
    sanitized_color = parse_color(color)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
    circle = Circle((0.5, 0.5), 0.4, color=sanitized_color)
    ax.add_patch(circle)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.savefig(output)
    plt.close(fig)

    return output
