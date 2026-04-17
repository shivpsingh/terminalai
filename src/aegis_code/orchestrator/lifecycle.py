"""Lifecycle helpers."""

from aegis_code.domain.enums import RunPhase


def next_phase_after_verification(success: bool) -> RunPhase:
    """Return next phase based on verification outcome."""

    return RunPhase.COMPLETION if success else RunPhase.REPAIR
