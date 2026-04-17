"""Run tests tool."""

import subprocess

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class RunTestsInput(BaseModel):
    cwd: str = "."
    command: str = "pytest -q"


class RunTestsTool(BaseTool):
    metadata = ToolMetadata(
        name="run_tests",
        description="Run project tests",
        risk=RiskLevel.MODERATE,
        requires_approval=True,
    )
    input_model = RunTestsInput

    async def execute(self, payload: RunTestsInput) -> ToolResult:
        result = subprocess.run(
            payload.command.split(),
            cwd=payload.cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return ToolResult(
            success=result.returncode == 0,
            output={"stdout": result.stdout, "stderr": result.stderr},
        )
