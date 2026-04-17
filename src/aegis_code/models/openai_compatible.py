"""OpenAI-compatible adapter skeleton."""

from aegis_code.domain.models import ModelRequest, ModelResponse
from aegis_code.models.base import ModelAdapter


class OpenAICompatibleAdapter(ModelAdapter):
    """Skeleton adapter for OpenAI-like APIs."""

    async def complete(self, request: ModelRequest) -> ModelResponse:
        raise NotImplementedError("wire provider client and normalize to ModelResponse")
