"""Explicit run state transitions."""

from aegis_code.domain.enums import RunPhase


class InvalidTransitionError(ValueError):
    """Raised when a transition is invalid."""


_TRANSITIONS: dict[RunPhase, set[RunPhase]] = {
    RunPhase.INTAKE: {RunPhase.PLANNING},
    RunPhase.PLANNING: {RunPhase.EXECUTION},
    RunPhase.EXECUTION: {RunPhase.VERIFICATION, RunPhase.REPAIR},
    RunPhase.VERIFICATION: {RunPhase.COMPLETION, RunPhase.REPAIR},
    RunPhase.REPAIR: {RunPhase.EXECUTION, RunPhase.COMPLETION},
    RunPhase.COMPLETION: set(),
}


def can_transition(current: RunPhase, new: RunPhase) -> bool:
    """Return true when transition is legal."""

    return new in _TRANSITIONS[current]


def transition(current: RunPhase, new: RunPhase) -> RunPhase:
    """Validate and return next phase."""

    if not can_transition(current, new):
        raise InvalidTransitionError(f"invalid transition: {current} -> {new}")
    return new
