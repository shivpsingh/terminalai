"""Risk classification helpers."""

from aegis_code.domain.enums import RiskLevel

DANGEROUS_TOKENS = {"rm", "sudo", "shutdown", "reboot"}


def classify_shell_command(command: str) -> RiskLevel:
    """Classify shell command risk."""

    tokens = set(command.split())
    if tokens & DANGEROUS_TOKENS:
        return RiskLevel.HIGH
    return RiskLevel.MODERATE if command else RiskLevel.SAFE
