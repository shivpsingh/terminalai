"""Search files tool."""

import re
from pathlib import Path

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class SearchFilesInput(BaseModel):
    root: str
    pattern: str


class SearchFilesTool(BaseTool):
    metadata = ToolMetadata(
        name="search_files",
        description="Search files with regex pattern",
        risk=RiskLevel.SAFE,
    )
    input_model = SearchFilesInput

    async def execute(self, payload: SearchFilesInput) -> ToolResult:
        regex = re.compile(payload.pattern)
        hits: list[dict[str, object]] = []
        for path in Path(payload.root).rglob("*"):
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for index, line in enumerate(text.splitlines(), start=1):
                if regex.search(line):
                    hits.append({"path": str(path), "line": index, "text": line})
        return ToolResult(success=True, output={"matches": hits})
