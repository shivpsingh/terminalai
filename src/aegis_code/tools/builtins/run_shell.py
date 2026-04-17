"""Run shell command tool."""

import shlex
import subprocess

from pydantic import BaseModel, Field

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class RunShellInput(BaseModel):
    command: str
    cwd: str = "."
    timeout_seconds: int = Field(default=30, ge=1, le=300)


class RunShellTool(BaseTool):
    metadata = ToolMetadata(
        name="run_shell",
        description="Run shell command with timeout",
        risk=RiskLevel.HIGH,
        requires_approval=True,
    )
    input_model = RunShellInput

    async def execute(self, payload: RunShellInput) -> ToolResult:
        args = shlex.split(payload.command)
        completed = subprocess.run(
            args,
            cwd=payload.cwd,
            capture_output=True,
            text=True,
            timeout=payload.timeout_seconds,
            check=False,
        )
        success = completed.returncode == 0
        return ToolResult(
            success=success,
            output={
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "code": completed.returncode,
            },
            error=None if success else "command failed",
        )
