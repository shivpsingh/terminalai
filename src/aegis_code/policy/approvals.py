"""Approval flow objects."""

from pydantic import BaseModel


class PolicyDecision(BaseModel):
    """Result of a policy evaluation."""

    allowed: bool
    requires_approval: bool = False
    reason: str = ""
