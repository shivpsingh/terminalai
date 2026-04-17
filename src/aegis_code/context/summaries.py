"""Summary helpers for prior steps."""


def summarize_lines(lines: list[str], max_lines: int = 3) -> str:
    """Build concise text summary."""

    selected = lines[:max_lines]
    return " | ".join(selected)
