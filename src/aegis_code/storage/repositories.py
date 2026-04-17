"""Repository implementations."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from aegis_code.domain.enums import EventType, PlanStepStatus, RunPhase, RunStatus
from aegis_code.domain.models import AgentRun, Checkpoint, PlanStep, RunEvent
from aegis_code.orchestrator.checkpointing import CheckpointRepository
from aegis_code.orchestrator.service import EventRepository, RunRepository
from aegis_code.storage.db import Database
from aegis_code.storage.tables import CheckpointTable, EventTable, PlanStepTable, RunTable


class SqliteRunRepository(RunRepository):
    """Run persistence backed by SQLite."""

    def __init__(self, db: Database) -> None:
        self.db = db

    def create_run(self, run: AgentRun) -> None:
        with self.db.session() as session:
            session.add(
                RunTable(
                    run_id=run.run_id,
                    request=run.request,
                    phase=run.phase.value,
                    status=run.status.value,
                    created_at=run.created_at,
                    updated_at=run.updated_at,
                )
            )
            session.commit()

    def update_run(self, run: AgentRun) -> None:
        with self.db.session() as session:
            row = session.get(RunTable, run.run_id)
            if row is None:
                raise KeyError(run.run_id)
            row.phase = run.phase.value
            row.status = run.status.value
            row.updated_at = run.updated_at
            session.commit()

    def get_run(self, run_id: str) -> AgentRun:
        with self.db.session() as session:
            row = session.get(RunTable, run_id)
            if row is None:
                raise KeyError(run_id)
            steps = self._list_steps(session, run_id)
            return AgentRun(
                run_id=row.run_id,
                request=row.request,
                phase=RunPhase(row.phase),
                status=RunStatus(row.status),
                plan_steps=steps,
                created_at=row.created_at,
                updated_at=row.updated_at,
            )

    def save_plan_steps(self, run_id: str, steps: list[PlanStep]) -> None:
        with self.db.session() as session:
            for step in steps:
                session.add(
                    PlanStepTable(
                        step_id=step.id,
                        run_id=run_id,
                        step_order=step.order,
                        title=step.title,
                        status=step.status.value,
                    )
                )
            session.commit()

    @staticmethod
    def _list_steps(session: Session, run_id: str) -> list[PlanStep]:
        result = session.execute(
            select(PlanStepTable)
            .where(PlanStepTable.run_id == run_id)
            .order_by(PlanStepTable.step_order)
        )
        return [
            PlanStep(
                id=row.step_id,
                run_id=row.run_id,
                order=row.step_order,
                title=row.title,
                status=PlanStepStatus(row.status),
            )
            for row in result.scalars().all()
        ]


class SqliteEventRepository(EventRepository):
    """Event persistence backed by SQLite."""

    def __init__(self, db: Database) -> None:
        self.db = db

    def add_event(self, event: RunEvent) -> None:
        with self.db.session() as session:
            session.add(
                EventTable(
                    run_id=event.run_id,
                    event_type=event.type.value,
                    message=event.message,
                    payload=event.payload,
                    created_at=event.created_at,
                )
            )
            session.commit()

    def list_events(self, run_id: str) -> list[RunEvent]:
        with self.db.session() as session:
            rows = session.execute(
                select(EventTable)
                .where(EventTable.run_id == run_id)
                .order_by(EventTable.created_at)
            ).scalars()
            return [
                RunEvent(
                    run_id=row.run_id,
                    type=EventType(row.event_type),
                    message=row.message,
                    payload=row.payload,
                    created_at=row.created_at,
                )
                for row in rows
            ]


class SqliteCheckpointRepository(CheckpointRepository):
    """Checkpoint persistence backed by SQLite."""

    def __init__(self, db: Database) -> None:
        self.db = db

    def save_checkpoint(self, checkpoint: Checkpoint) -> None:
        with self.db.session() as session:
            session.add(
                CheckpointTable(
                    checkpoint_id=checkpoint.id,
                    run_id=checkpoint.run_id,
                    phase=checkpoint.phase.value,
                    data=checkpoint.data,
                    created_at=checkpoint.created_at,
                )
            )
            session.commit()

    def load_latest_checkpoint(self, run_id: str) -> Checkpoint | None:
        with self.db.session() as session:
            row = (
                session.execute(
                    select(CheckpointTable)
                    .where(CheckpointTable.run_id == run_id)
                    .order_by(CheckpointTable.created_at.desc())
                )
                .scalars()
                .first()
            )
            if row is None:
                return None
            return Checkpoint(
                id=row.checkpoint_id,
                run_id=row.run_id,
                phase=RunPhase(row.phase),
                data=row.data,
            )
