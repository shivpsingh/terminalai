"""Worker agent abstraction for future parallel execution."""

from aegis_code.agents.base import BaseAgent
from aegis_code.domain.models import ModelRequest, ModelResponse


class WorkerAgent(BaseAgent):
    """Placeholder worker agent."""

    async def think(self, request: ModelRequest) -> ModelResponse:
        return await self.model.complete(request)
