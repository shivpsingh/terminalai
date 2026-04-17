"""Lead agent coordinates plan, execution, verification, repair."""

from aegis_code.agents.planner import Planner
from aegis_code.agents.repairer import Repairer
from aegis_code.agents.verifier import Verifier
from aegis_code.domain.models import PlanStep, ToolResult, VerificationResult


class LeadAgent:
    """Lead role orchestrating worker-like actions for MVP."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.verifier = Verifier()
        self.repairer = Repairer()

    def plan(self, request: str, run_id: str) -> list[PlanStep]:
        """Build a sequential plan."""

        return self.planner.build_plan(request, run_id=run_id)

    async def execute_step(self, step: PlanStep) -> ToolResult:
        """Execute a step. MVP marks success."""

        return ToolResult(success=True, output={"step": step.title})

    def verify(self, steps: list[PlanStep]) -> VerificationResult:
        """Verify plan outcomes."""

        return self.verifier.verify(steps)

    def repair(self, reason: str) -> None:
        """Record repair attempt."""

        self.repairer.attempt(run_id="unknown", reason=reason)
