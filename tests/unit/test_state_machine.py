import pytest

from aegis_code.domain.enums import RunPhase
from aegis_code.orchestrator.state_machine import InvalidTransitionError, transition


def test_valid_transition() -> None:
    assert transition(RunPhase.INTAKE, RunPhase.PLANNING) == RunPhase.PLANNING


def test_invalid_transition_raises() -> None:
    with pytest.raises(InvalidTransitionError):
        transition(RunPhase.INTAKE, RunPhase.EXECUTION)
