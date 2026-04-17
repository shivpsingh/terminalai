"""Read file tool."""

from pathlib import Path

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class ReadFileInput(BaseModel):
    path: str


class ReadFileTool(BaseTool):
    metadata = ToolMetadata(
        name="read_file",
        description="Read text file content",
        risk=RiskLevel.SAFE,
    )
    input_model = ReadFileInput

    async def execute(self, payload: ReadFileInput) -> ToolResult:
        content = Path(payload.path).read_text(encoding="utf-8")
        return ToolResult(success=True, output={"content": content})
