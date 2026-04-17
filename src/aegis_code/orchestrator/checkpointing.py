"""Checkpoint save/load behavior."""

from aegis_code.domain.enums import RunPhase
from aegis_code.domain.ids import new_checkpoint_id
from aegis_code.domain.models import Checkpoint


class CheckpointStore:
    """Simple checkpoint service wrapper."""

    def __init__(self, repo: "CheckpointRepository") -> None:
        self.repo = repo

    def save(self, run_id: str, phase: RunPhase, data: dict[str, object]) -> Checkpoint:
        """Persist a checkpoint."""

        checkpoint = Checkpoint(id=new_checkpoint_id(), run_id=run_id, phase=phase, data=data)
        self.repo.save_checkpoint(checkpoint)
        return checkpoint

    def load_latest(self, run_id: str) -> Checkpoint | None:
        """Load latest checkpoint."""

        return self.repo.load_latest_checkpoint(run_id)


class CheckpointRepository:
    """Protocol-like interface for checkpoint persistence."""

    def save_checkpoint(self, checkpoint: Checkpoint) -> None:
        raise NotImplementedError

    def load_latest_checkpoint(self, run_id: str) -> Checkpoint | None:
        raise NotImplementedError
