"""Provider-agnostic model interface."""

from abc import ABC, abstractmethod

from aegis_code.domain.models import ModelRequest, ModelResponse


class ModelAdapter(ABC):
    """Normalized model adapter interface."""

    @abstractmethod
    async def complete(self, request: ModelRequest) -> ModelResponse:
        """Return a normalized model response."""
