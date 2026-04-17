"""Web lookup placeholder."""

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata


class WebLookupInput(BaseModel):
    query: str


class WebLookupTool(BaseTool):
    metadata = ToolMetadata(
        name="web_lookup",
        description="Placeholder for future web retrieval",
        risk=RiskLevel.MODERATE,
        requires_approval=True,
    )
    input_model = WebLookupInput

    async def execute(self, payload: WebLookupInput) -> ToolResult:
        return ToolResult(success=False, output={"query": payload.query}, error="not implemented")
