"""Run command."""

import asyncio

import typer

from aegis_code.services.run_service import RunService


def run_command(request: str) -> None:
    """Run a request through orchestrator."""

    service = RunService.build_default()
    result = asyncio.run(service.run(request))
    typer.echo(f"Run {result.run_id}: {result.status.value}")
    for step in result.plan_steps:
        typer.echo(f"- {step.title}: {step.status.value}")
