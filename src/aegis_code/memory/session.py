"""Session memory store."""

from aegis_code.domain.models import MemoryRecord


class SessionMemory:
    """In-memory session memory implementation."""

    def __init__(self) -> None:
        self.records: list[MemoryRecord] = []

    def add(self, record: MemoryRecord) -> None:
        self.records.append(record)

    def values(self) -> list[str]:
        return [record.value for record in self.records]
