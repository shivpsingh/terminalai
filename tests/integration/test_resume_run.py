import asyncio

from aegis_code.agents.lead_agent import LeadAgent
from aegis_code.orchestrator.checkpointing import CheckpointStore
from aegis_code.orchestrator.service import OrchestratorService
from aegis_code.storage.repositories import (
    SqliteCheckpointRepository,
    SqliteEventRepository,
    SqliteRunRepository,
)


def test_resume_flow(test_db) -> None:
    orchestrator = OrchestratorService(
        lead_agent=LeadAgent(),
        checkpoint_store=CheckpointStore(SqliteCheckpointRepository(test_db)),
        run_repo=SqliteRunRepository(test_db),
        event_repo=SqliteEventRepository(test_db),
    )

    created = asyncio.run(orchestrator.run("run once"))
    resumed = asyncio.run(orchestrator.resume(created.run_id))

    assert resumed.run_id == created.run_id
