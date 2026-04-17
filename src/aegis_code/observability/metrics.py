"""Metrics snapshot model."""

from pydantic import BaseModel


class MetricsSnapshot(BaseModel):
    """MVP metrics snapshot."""

    tool_success: int = 0
    tool_failure: int = 0
    total_latency_ms: int = 0
