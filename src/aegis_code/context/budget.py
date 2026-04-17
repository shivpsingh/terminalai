"""Context budget modeling."""

from pydantic import BaseModel


class ContextBudget(BaseModel):
    """Approximate token budget for context assembly."""

    max_tokens: int = 4000

    @staticmethod
    def estimate_tokens(text: str) -> int:
        """Rough token estimate used in MVP."""

        return max(1, len(text) // 4)

    def fits(self, pieces: list[str]) -> bool:
        """Return true when all pieces fit budget."""

        used = sum(self.estimate_tokens(piece) for piece in pieces)
        return used <= self.max_tokens
