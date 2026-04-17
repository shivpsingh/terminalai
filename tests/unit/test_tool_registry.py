from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult
from aegis_code.tools.base import BaseTool, ToolMetadata
from aegis_code.tools.registry import ToolRegistry


class _Input(BaseModel):
    value: str


class _Tool(BaseTool):
    metadata = ToolMetadata(name="dummy", description="", risk=RiskLevel.SAFE)
    input_model = _Input

    async def execute(self, payload: _Input) -> ToolResult:
        return ToolResult(success=True, output={"value": payload.value})


def test_registry_register_and_get() -> None:
    registry = ToolRegistry()
    registry.register(_Tool())
    tool = registry.get("dummy")
    assert tool.metadata.name == "dummy"
    assert registry.list_names() == ["dummy"]
