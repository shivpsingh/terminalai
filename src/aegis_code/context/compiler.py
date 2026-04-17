"""Context compilation entrypoint."""

from aegis_code.context.budget import ContextBudget
from aegis_code.context.selectors import select_recent_items
from aegis_code.domain.models import ContextBundle


class ContextCompiler:
    """Assemble context from memory and runtime inputs."""

    def __init__(self, budget: ContextBudget | None = None) -> None:
        self.budget = budget or ContextBudget()

    def compile(
        self,
        run_id: str,
        request: str,
        project_instructions: str,
        session_memory: list[str],
        repo_memory: list[str],
        selected_files: list[str],
        prior_summaries: list[str],
        recent_tool_outputs: list[str],
    ) -> ContextBundle:
        """Compile and prune context into a bundle."""

        pieces = [
            project_instructions,
            *select_recent_items(session_memory),
            *select_recent_items(repo_memory),
            *selected_files,
            *prior_summaries,
            *select_recent_items(recent_tool_outputs),
        ]
        snippets: list[str] = []
        for piece in pieces:
            candidate = [*snippets, piece]
            if self.budget.fits(candidate):
                snippets.append(piece)
        estimated = sum(self.budget.estimate_tokens(piece) for piece in snippets)
        return ContextBundle(
            run_id=run_id,
            request=request,
            snippets=snippets,
            max_tokens=self.budget.max_tokens,
            estimated_tokens=estimated,
        )
