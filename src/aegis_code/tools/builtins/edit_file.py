"""Edit file tool."""

from pathlib import Path

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class EditFileInput(BaseModel):
    path: str
    old: str
    new: str


class EditFileTool(BaseTool):
    metadata = ToolMetadata(
        name="edit_file",
        description="Replace text in file",
        risk=RiskLevel.MODERATE,
        requires_approval=True,
    )
    input_model = EditFileInput

    async def execute(self, payload: EditFileInput) -> ToolResult:
        path = Path(payload.path)
        content = path.read_text(encoding="utf-8")
        if payload.old not in content:
            return ToolResult(success=False, output={}, error="target text not found")
        updated = content.replace(payload.old, payload.new)
        path.write_text(updated, encoding="utf-8")
        return ToolResult(success=True, output={"path": str(path)})
