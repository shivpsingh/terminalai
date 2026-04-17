"""Clock utility."""

from datetime import UTC, datetime


def now_utc() -> datetime:
    """Return current UTC timestamp."""

    return datetime.now(UTC)
