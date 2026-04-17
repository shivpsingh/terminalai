"""Tool execution runtime with policy checks."""

from __future__ import annotations

from typing import Protocol

from aegis_code.domain.enums import EventType
from aegis_code.domain.events import build_event
from aegis_code.domain.models import RunEvent, ToolResult
from aegis_code.policy.engine import PolicyEngine
from aegis_code.tools.registry import ToolRegistry


class ToolExecutor:
    """Coordinates tool validation, policy, execution, and events."""

    def __init__(
        self,
        registry: ToolRegistry,
        policy: PolicyEngine,
        event_repo: EventRepository,
    ) -> None:
        self.registry = registry
        self.policy = policy
        self.event_repo = event_repo

    async def call(self, run_id: str, tool_name: str, payload: dict[str, object]) -> ToolResult:
        """Execute one tool call through policy guard."""

        tool = self.registry.get(tool_name)
        decision = self.policy.evaluate(tool.metadata, payload)
        self.event_repo.add_event(
            build_event(run_id, EventType.TOOL_CALLED, f"tool called: {tool_name}")
        )
        if not decision.allowed:
            self.event_repo.add_event(
                build_event(run_id, EventType.TOOL_FAILED, f"tool denied: {tool_name}")
            )
            return ToolResult(success=False, output={}, error=decision.reason)

        validated = tool.validate_input(payload)
        result = await tool.execute(validated)
        event_type = EventType.TOOL_SUCCEEDED if result.success else EventType.TOOL_FAILED
        self.event_repo.add_event(build_event(run_id, event_type, f"tool finished: {tool_name}"))
        return result


class EventRepository(Protocol):
    """Event repository contract."""

    def add_event(self, event: RunEvent) -> None:
        ...
