"""Main orchestrator service."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Protocol

from aegis_code.agents.lead_agent import LeadAgent
from aegis_code.domain.enums import EventType, PlanStepStatus, RunPhase, RunStatus
from aegis_code.domain.events import build_event
from aegis_code.domain.ids import new_run_id
from aegis_code.domain.models import AgentRun, PlanStep, RunEvent
from aegis_code.orchestrator.checkpointing import CheckpointStore
from aegis_code.orchestrator.lifecycle import next_phase_after_verification
from aegis_code.orchestrator.state_machine import transition


class OrchestratorService:
    """Coordinates run lifecycle for MVP."""

    def __init__(
        self,
        lead_agent: LeadAgent,
        checkpoint_store: CheckpointStore,
        run_repo: RunRepository,
        event_repo: EventRepository,
    ) -> None:
        self.lead_agent = lead_agent
        self.checkpoint_store = checkpoint_store
        self.run_repo = run_repo
        self.event_repo = event_repo

    async def run(self, request: str) -> AgentRun:
        """Run full lifecycle from intake to completion."""

        run = AgentRun(run_id=new_run_id(), request=request, status=RunStatus.RUNNING)
        self.run_repo.create_run(run)
        self.event_repo.add_event(build_event(run.run_id, EventType.RUN_CREATED, "run created"))

        run.phase = transition(run.phase, RunPhase.PLANNING)
        plan_steps = self.lead_agent.plan(request, run.run_id)
        run.plan_steps = plan_steps
        self.run_repo.save_plan_steps(run.run_id, plan_steps)
        self.event_repo.add_event(build_event(run.run_id, EventType.PLAN_CREATED, "plan created"))
        self.checkpoint_store.save(
            run.run_id,
            run.phase,
            {"steps": [s.model_dump() for s in plan_steps]},
        )

        run.phase = transition(run.phase, RunPhase.EXECUTION)
        for step in run.plan_steps:
            self.event_repo.add_event(
                build_event(run.run_id, EventType.PLAN_STEP_STARTED, f"step started: {step.title}")
            )
            step.status = PlanStepStatus.RUNNING
            result = await self.lead_agent.execute_step(step)
            step.status = PlanStepStatus.COMPLETED if result.success else PlanStepStatus.FAILED
            self.event_repo.add_event(
                build_event(run.run_id, EventType.PLAN_STEP_COMPLETED, f"step done: {step.title}")
            )

        run.phase = transition(run.phase, RunPhase.VERIFICATION)
        verification = self.lead_agent.verify(run.plan_steps)
        run.phase = transition(run.phase, next_phase_after_verification(verification.success))

        if run.phase == RunPhase.REPAIR:
            self.lead_agent.repair("verification failed")
            run.phase = transition(run.phase, RunPhase.COMPLETION)

        run.status = RunStatus.COMPLETED
        run.phase = RunPhase.COMPLETION
        run.updated_at = datetime.now(UTC)
        self.run_repo.update_run(run)
        self.event_repo.add_event(build_event(run.run_id, EventType.RUN_COMPLETED, "run completed"))
        self.checkpoint_store.save(run.run_id, run.phase, {"status": run.status.value})
        return run

    async def resume(self, run_id: str) -> AgentRun:
        """Resume from latest checkpoint; MVP returns persisted run."""

        checkpoint = self.checkpoint_store.load_latest(run_id)
        run = self.run_repo.get_run(run_id)
        if checkpoint is not None:
            self.event_repo.add_event(build_event(run_id, EventType.RUN_RESUMED, "run resumed"))
        return run

    def replay(self, run_id: str) -> list[RunEvent]:
        """Return persisted events for replay."""

        return self.event_repo.list_events(run_id)


class RunRepository(Protocol):
    """Run persistence contract."""

    def create_run(self, run: AgentRun) -> None:
        ...

    def update_run(self, run: AgentRun) -> None:
        ...

    def get_run(self, run_id: str) -> AgentRun:
        ...

    def save_plan_steps(self, run_id: str, steps: list[PlanStep]) -> None:
        ...


class EventRepository(Protocol):
    """Event persistence contract."""

    def add_event(self, event: RunEvent) -> None:
        ...

    def list_events(self, run_id: str) -> list[RunEvent]:
        ...
