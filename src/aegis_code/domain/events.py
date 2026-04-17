"""Event helpers."""

from aegis_code.domain.enums import EventType
from aegis_code.domain.models import RunEvent


def build_event(run_id: str, event_type: EventType, message: str) -> RunEvent:
    """Build a minimal event object."""

    return RunEvent(run_id=run_id, type=event_type, message=message)
