"""Planning behavior."""

from aegis_code.domain.ids import new_step_id
from aegis_code.domain.models import PlanStep


class Planner:
    """Simple deterministic planner for MVP."""

    def build_plan(self, request: str, run_id: str = "plan_preview") -> list[PlanStep]:
        """Create minimal sequential plan."""

        return [
            PlanStep(
                id=new_step_id(),
                run_id=run_id,
                order=1,
                title="Understand task",
                details=request,
            ),
            PlanStep(
                id=new_step_id(),
                run_id=run_id,
                order=2,
                title="Execute requested change",
            ),
            PlanStep(
                id=new_step_id(),
                run_id=run_id,
                order=3,
                title="Verify outcome",
            ),
        ]
