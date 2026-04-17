"""Mock model adapter for deterministic local testing."""

from aegis_code.domain.models import ModelRequest, ModelResponse
from aegis_code.models.base import ModelAdapter


class MockAdapter(ModelAdapter):
    """Echoes prompt while providing fake usage data."""

    async def complete(self, request: ModelRequest) -> ModelResponse:
        return ModelResponse(
            text=f"Mock response for: {request.prompt}",
            input_tokens=request.context.estimated_tokens,
            output_tokens=32,
            latency_ms=5,
        )
