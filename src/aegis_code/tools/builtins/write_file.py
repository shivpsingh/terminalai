"""Write file tool."""

from pathlib import Path

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class WriteFileInput(BaseModel):
    path: str
    content: str


class WriteFileTool(BaseTool):
    metadata = ToolMetadata(
        name="write_file",
        description="Write content to file",
        risk=RiskLevel.MODERATE,
        requires_approval=True,
    )
    input_model = WriteFileInput

    async def execute(self, payload: WriteFileInput) -> ToolResult:
        path = Path(payload.path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload.content, encoding="utf-8")
        return ToolResult(success=True, output={"path": str(path)})
