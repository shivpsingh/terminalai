from aegis_code.domain.enums import RunPhase
from aegis_code.orchestrator.checkpointing import CheckpointStore
from aegis_code.storage.repositories import SqliteCheckpointRepository


def test_checkpoint_save_and_load(test_db) -> None:
    repo = SqliteCheckpointRepository(test_db)
    store = CheckpointStore(repo)

    checkpoint = store.save("run_1", RunPhase.PLANNING, {"k": "v"})
    loaded = store.load_latest("run_1")

    assert loaded is not None
    assert loaded.id == checkpoint.id
    assert loaded.phase == RunPhase.PLANNING
