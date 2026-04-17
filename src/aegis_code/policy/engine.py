"""Policy engine implementation."""

from aegis_code.domain.enums import ApprovalMode, RiskLevel
from aegis_code.policy.approvals import PolicyDecision
from aegis_code.policy.rules import within_workspace
from aegis_code.tools.base import ToolMetadata


class PolicyEngine:
    """Evaluate tool calls against approval mode and risk."""

    def __init__(
        self,
        mode: ApprovalMode = ApprovalMode.AUTO_APPROVE_SAFE,
        workspace_root: str = ".",
    ) -> None:
        self.mode = mode
        self.workspace_root = workspace_root

    def evaluate(self, metadata: ToolMetadata, payload: dict[str, object]) -> PolicyDecision:
        """Return allow/deny decision."""

        if (
            "path" in payload
            and isinstance(payload["path"], str)
            and not within_workspace(payload["path"], self.workspace_root)
        ):
            return PolicyDecision(allowed=False, reason="path outside workspace")

        if self.mode == ApprovalMode.FULL_ACCESS:
            return PolicyDecision(allowed=True)

        if self.mode == ApprovalMode.READ_ONLY:
            if metadata.risk in {RiskLevel.MODERATE, RiskLevel.HIGH}:
                return PolicyDecision(
                    allowed=False,
                    reason="read_only mode blocks mutating/risky tools",
                )
            return PolicyDecision(allowed=True)

        if self.mode == ApprovalMode.ASK_EVERY_TIME:
            return PolicyDecision(allowed=True, requires_approval=True, reason="approval required")

        # AUTO_APPROVE_SAFE
        if metadata.risk == RiskLevel.SAFE and not metadata.requires_approval:
            return PolicyDecision(allowed=True)
        return PolicyDecision(
            allowed=True,
            requires_approval=True,
            reason="approval required for risky tool",
        )
