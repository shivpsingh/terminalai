"""Run service that wires concrete components."""

from aegis_code.agents.lead_agent import LeadAgent
from aegis_code.domain.models import AgentRun, RunEvent
from aegis_code.orchestrator.checkpointing import CheckpointStore
from aegis_code.orchestrator.service import OrchestratorService
from aegis_code.storage.db import Database
from aegis_code.storage.repositories import (
    SqliteCheckpointRepository,
    SqliteEventRepository,
    SqliteRunRepository,
)


class RunService:
    """Application service for CLI use."""

    def __init__(self, orchestrator: OrchestratorService) -> None:
        self.orchestrator = orchestrator

    @classmethod
    def build_default(cls) -> "RunService":
        """Build service graph with SQLite persistence."""

        db = Database()
        db.create_all()
        run_repo = SqliteRunRepository(db)
        event_repo = SqliteEventRepository(db)
        checkpoint_repo = SqliteCheckpointRepository(db)
        orchestrator = OrchestratorService(
            lead_agent=LeadAgent(),
            checkpoint_store=CheckpointStore(checkpoint_repo),
            run_repo=run_repo,
            event_repo=event_repo,
        )
        return cls(orchestrator)

    async def run(self, request: str) -> AgentRun:
        """Start a new run."""

        return await self.orchestrator.run(request)

    async def resume(self, run_id: str) -> AgentRun:
        """Resume existing run."""

        return await self.orchestrator.resume(run_id)

    def replay(self, run_id: str) -> list[RunEvent]:
        """Replay run events."""

        return self.orchestrator.replay(run_id)
