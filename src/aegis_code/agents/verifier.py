"""Verification behavior."""

from aegis_code.domain.enums import PlanStepStatus
from aegis_code.domain.models import PlanStep, VerificationResult


class Verifier:
    """Checks whether all plan steps completed."""

    def verify(self, steps: list[PlanStep]) -> VerificationResult:
        """Return success if no failed steps."""

        failed = [step.title for step in steps if step.status == PlanStepStatus.FAILED]
        return VerificationResult(success=not failed, findings=failed)
