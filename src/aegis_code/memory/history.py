"""Run history summaries."""


class RunHistory:
    """Summarized run history in memory."""

    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, summary: str) -> None:
        self.items.append(summary)

    def latest(self, limit: int = 5) -> list[str]:
        return self.items[-limit:]
