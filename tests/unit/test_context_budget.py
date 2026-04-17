from aegis_code.context.budget import ContextBudget


def test_budget_estimate_and_fit() -> None:
    budget = ContextBudget(max_tokens=10)
    assert budget.estimate_tokens("abcd") == 1
    assert budget.fits(["abcd", "efgh"])
    assert not budget.fits(["a" * 100])
