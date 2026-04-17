"""Approval handling service."""

from aegis_code.policy.approvals import PolicyDecision


class ApprovalService:
    """MVP approval service; defaults to grant when asked."""

    def resolve(self, decision: PolicyDecision) -> bool:
        """Resolve approval decision."""

        return decision.allowed
