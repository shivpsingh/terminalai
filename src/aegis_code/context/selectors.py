"""Context selection helpers."""


def select_recent_items(items: list[str], limit: int = 5) -> list[str]:
    """Select most recent items by list position."""

    return items[-limit:]
