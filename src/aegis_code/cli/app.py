"""Typer application entrypoint."""

import typer

from aegis_code.cli.commands.plan import plan_command
from aegis_code.cli.commands.replay import replay_command
from aegis_code.cli.commands.resume import resume_command
from aegis_code.cli.commands.run import run_command

app = typer.Typer(help="Aegis Code CLI")
app.command("run")(run_command)
app.command("plan")(plan_command)
app.command("resume")(resume_command)
app.command("replay")(replay_command)

if __name__ == "__main__":
    app()
