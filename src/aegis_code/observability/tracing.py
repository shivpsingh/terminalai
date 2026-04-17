"""In-memory tracing model."""

from aegis_code.domain.models import RunEvent


class TraceBuffer:
    """Simple trace buffer used for snapshots and tests."""

    def __init__(self) -> None:
        self.events: list[RunEvent] = []

    def add(self, event: RunEvent) -> None:
        self.events.append(event)
