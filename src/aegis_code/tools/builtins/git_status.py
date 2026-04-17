"""Git status tool."""

import subprocess

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class GitStatusInput(BaseModel):
    cwd: str = "."


class GitStatusTool(BaseTool):
    metadata = ToolMetadata(
        name="git_status",
        description="Show git status",
        risk=RiskLevel.SAFE,
    )
    input_model = GitStatusInput

    async def execute(self, payload: GitStatusInput) -> ToolResult:
        result = subprocess.run(
            ["git", "--no-pager", "status", "--short"],
            cwd=payload.cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return ToolResult(success=result.returncode == 0, output={"stdout": result.stdout})
