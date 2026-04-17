"""Replay command."""

import typer

from aegis_code.services.run_service import RunService


def replay_command(run_id: str) -> None:
    """Replay events for a run."""

    service = RunService.build_default()
    events = service.replay(run_id)
    for event in events:
        typer.echo(f"{event.type.value}: {event.message}")
