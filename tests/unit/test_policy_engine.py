from aegis_code.domain.enums import ApprovalMode, RiskLevel
from aegis_code.policy.engine import PolicyEngine
from aegis_code.tools.base import ToolMetadata


def test_read_only_blocks_write_tools() -> None:
    engine = PolicyEngine(mode=ApprovalMode.READ_ONLY)
    metadata = ToolMetadata(name="write_file", description="", risk=RiskLevel.MODERATE)
    decision = engine.evaluate(metadata, {"path": "./x.txt"})
    assert not decision.allowed


def test_auto_approve_safe_tool() -> None:
    engine = PolicyEngine(mode=ApprovalMode.AUTO_APPROVE_SAFE)
    metadata = ToolMetadata(name="read_file", description="", risk=RiskLevel.SAFE)
    decision = engine.evaluate(metadata, {"path": "./README.md"})
    assert decision.allowed
    assert not decision.requires_approval
