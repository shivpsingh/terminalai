"""Repair behavior."""

from aegis_code.domain.models import RepairAttempt


class Repairer:
    """Records repair attempts."""

    def attempt(self, run_id: str, reason: str, attempt: int = 1) -> RepairAttempt:
        """Build repair attempt model."""

        return RepairAttempt(run_id=run_id, attempt=attempt, reason=reason)
