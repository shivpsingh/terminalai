"""Filesystem helpers."""

from pathlib import Path


def ensure_parent(path: str) -> None:
    """Ensure parent directory exists."""

    Path(path).parent.mkdir(parents=True, exist_ok=True)
