"""Base agent definitions."""

from abc import ABC, abstractmethod

from aegis_code.domain.models import ModelRequest, ModelResponse
from aegis_code.models.base import ModelAdapter


class BaseAgent(ABC):
    """Base class for all agent roles."""

    def __init__(self, model: ModelAdapter) -> None:
        self.model = model

    @abstractmethod
    async def think(self, request: ModelRequest) -> ModelResponse:
        """Produce a model response."""
