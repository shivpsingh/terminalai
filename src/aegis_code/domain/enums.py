"""Domain enumerations."""

from enum import StrEnum


class RunPhase(StrEnum):
    INTAKE = "intake"
    PLANNING = "planning"
    EXECUTION = "execution"
    VERIFICATION = "verification"
    REPAIR = "repair"
    COMPLETION = "completion"


class RunStatus(StrEnum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"


class PlanStepStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class RiskLevel(StrEnum):
    SAFE = "safe"
    MODERATE = "moderate"
    HIGH = "high"


class ApprovalMode(StrEnum):
    ASK_EVERY_TIME = "ask_every_time"
    AUTO_APPROVE_SAFE = "auto_approve_safe"
    READ_ONLY = "read_only"
    FULL_ACCESS = "full_access"


class ApprovalDecisionType(StrEnum):
    GRANTED = "granted"
    DENIED = "denied"


class EventType(StrEnum):
    RUN_CREATED = "run.created"
    RUN_STARTED = "run.started"
    RUN_PAUSED = "run.paused"
    RUN_RESUMED = "run.resumed"
    RUN_COMPLETED = "run.completed"
    RUN_FAILED = "run.failed"
    PLAN_CREATED = "plan.created"
    PLAN_STEP_STARTED = "plan.step.started"
    PLAN_STEP_COMPLETED = "plan.step.completed"
    TOOL_CALLED = "tool.called"
    TOOL_SUCCEEDED = "tool.succeeded"
    TOOL_FAILED = "tool.failed"
    APPROVAL_REQUESTED = "approval.requested"
    APPROVAL_GRANTED = "approval.granted"
    APPROVAL_DENIED = "approval.denied"
    CHECKPOINT_CREATED = "checkpoint.created"
    RECOVERY_STARTED = "recovery.started"
    RECOVERY_COMPLETED = "recovery.completed"
