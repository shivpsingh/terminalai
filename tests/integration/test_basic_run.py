import asyncio

from aegis_code.agents.lead_agent import LeadAgent
from aegis_code.orchestrator.checkpointing import CheckpointStore
from aegis_code.orchestrator.service import OrchestratorService
from aegis_code.storage.repositories import (
    SqliteCheckpointRepository,
    SqliteEventRepository,
    SqliteRunRepository,
)


def test_basic_run_lifecycle(test_db) -> None:
    orchestrator = OrchestratorService(
        lead_agent=LeadAgent(),
        checkpoint_store=CheckpointStore(SqliteCheckpointRepository(test_db)),
        run_repo=SqliteRunRepository(test_db),
        event_repo=SqliteEventRepository(test_db),
    )

    run = asyncio.run(orchestrator.run("do a simple task"))
    assert run.status.value == "completed"
    assert len(run.plan_steps) == 3
