"""Common tool interface."""

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

from aegis_code.domain.enums import RiskLevel
from aegis_code.domain.models import ToolResult


class ToolMetadata(BaseModel):
    """Tool metadata used by policy and UX."""

    name: str
    description: str
    risk: RiskLevel
    requires_approval: bool = False


class BaseTool(ABC):
    """Base class for built-in and extension tools."""

    metadata: ToolMetadata
    input_model: type[BaseModel]

    @abstractmethod
    async def execute(self, payload: Any) -> ToolResult:
        """Execute tool action and return structured result."""

    def validate_input(self, payload: dict[str, Any]) -> BaseModel:
        """Validate tool input."""

        return self.input_model.model_validate(payload)
