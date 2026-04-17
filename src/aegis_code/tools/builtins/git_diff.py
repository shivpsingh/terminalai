"""Git diff tool."""

import subprocess

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class GitDiffInput(BaseModel):
    cwd: str = "."


class GitDiffTool(BaseTool):
    metadata = ToolMetadata(
        name="git_diff",
        description="Show git diff",
        risk=RiskLevel.SAFE,
    )
    input_model = GitDiffInput

    async def execute(self, payload: GitDiffInput) -> ToolResult:
        result = subprocess.run(
            ["git", "--no-pager", "diff"],
            cwd=payload.cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return ToolResult(success=result.returncode == 0, output={"stdout": result.stdout})
