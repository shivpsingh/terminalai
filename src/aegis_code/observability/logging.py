"""Structured logging setup."""

import structlog


def configure_logging() -> None:
    """Configure structlog for JSON-like event logs."""

    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ]
    )
