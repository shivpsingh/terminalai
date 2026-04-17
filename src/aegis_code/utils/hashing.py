"""Hashing helpers."""

import hashlib


def sha256_text(value: str) -> str:
    """Return SHA-256 hex digest for text."""

    return hashlib.sha256(value.encode("utf-8")).hexdigest()
