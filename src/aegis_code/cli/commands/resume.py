"""Resume command."""

import asyncio

import typer

from aegis_code.services.run_service import RunService


def resume_command(run_id: str) -> None:
    """Resume a run from latest checkpoint."""

    service = RunService.build_default()
    result = asyncio.run(service.resume(run_id))
    typer.echo(f"Resumed {result.run_id}: {result.status.value}")
