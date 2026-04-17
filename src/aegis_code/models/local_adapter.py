"""Local model adapter skeleton."""

from aegis_code.domain.models import ModelRequest, ModelResponse
from aegis_code.models.base import ModelAdapter


class LocalAdapter(ModelAdapter):
    """Skeleton adapter for local inference runtimes."""

    async def complete(self, request: ModelRequest) -> ModelResponse:
        raise NotImplementedError("wire local backend and normalize to ModelResponse")
