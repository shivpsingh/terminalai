"""Task graph behavior."""

from aegis_code.domain.models import PlanStep, TaskGraph


class SequentialTaskGraph:
    """Simple sequential graph implementation for MVP."""

    def __init__(self, graph: TaskGraph) -> None:
        self.graph = graph

    def ordered_steps(self) -> list[PlanStep]:
        """Return steps in execution order."""

        return sorted(self.graph.steps, key=lambda step: step.order)
