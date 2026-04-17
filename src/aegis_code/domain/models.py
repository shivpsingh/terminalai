"""Core typed domain models."""

from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, Field

from aegis_code.domain.enums import (
    ApprovalDecisionType,
    EventType,
    PlanStepStatus,
    RunPhase,
    RunStatus,
)


class Task(BaseModel):
    """User task request."""

    id: str
    run_id: str
    request: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class PlanStep(BaseModel):
    """Single plan unit."""

    id: str
    run_id: str
    order: int
    title: str
    status: PlanStepStatus = PlanStepStatus.PENDING
    details: str = ""


class TaskGraph(BaseModel):
    """Sequential task graph for MVP."""

    run_id: str
    steps: list[PlanStep]


class WorkerAssignment(BaseModel):
    """Worker assignment abstraction for future team mode."""

    worker_id: str
    step_id: str


class ToolCall(BaseModel):
    """Tool invocation details."""

    run_id: str
    step_id: str | None = None
    tool_name: str
    input_payload: dict[str, Any]
    called_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ToolResult(BaseModel):
    """Structured tool output."""

    success: bool
    output: dict[str, Any]
    error: str | None = None
    latency_ms: int = 0


class ApprovalRequest(BaseModel):
    """Human approval request."""

    run_id: str
    tool_name: str
    reason: str
    payload: dict[str, Any]


class ApprovalDecision(BaseModel):
    """Human approval decision."""

    run_id: str
    decision: ApprovalDecisionType
    reason: str = ""


class Checkpoint(BaseModel):
    """Recoverable run checkpoint."""

    id: str
    run_id: str
    phase: RunPhase
    data: dict[str, Any]
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class RunEvent(BaseModel):
    """Persisted event trace."""

    run_id: str
    type: EventType
    message: str
    payload: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class MemoryRecord(BaseModel):
    """Memory item for session/repo/history."""

    run_id: str
    scope: str
    key: str
    value: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ContextBundle(BaseModel):
    """Compiled context for model calls."""

    run_id: str
    request: str
    snippets: list[str]
    max_tokens: int
    estimated_tokens: int


class ModelRequest(BaseModel):
    """Normalized model request."""

    run_id: str
    prompt: str
    context: ContextBundle


class ModelResponse(BaseModel):
    """Normalized model response."""

    text: str
    tool_calls: list[dict[str, Any]] = Field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: int = 0


class VerificationResult(BaseModel):
    """Verification result for execution."""

    success: bool
    findings: list[str] = Field(default_factory=list)


class RepairAttempt(BaseModel):
    """Repair attempt metadata."""

    run_id: str
    attempt: int
    reason: str


class AgentRun(BaseModel):
    """Top-level run object."""

    run_id: str
    request: str
    phase: RunPhase = RunPhase.INTAKE
    status: RunStatus = RunStatus.CREATED
    plan_steps: list[PlanStep] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
