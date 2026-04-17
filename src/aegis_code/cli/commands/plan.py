"""Plan command."""

import typer

from aegis_code.agents.planner import Planner


def plan_command(request: str) -> None:
    """Display a simple plan without execution."""

    steps = Planner().build_plan(request)
    typer.echo("Plan:")
    for step in steps:
        typer.echo(f"- {step.order}. {step.title}")
