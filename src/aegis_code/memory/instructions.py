"""Project instruction store."""


class ProjectInstructions:
    """Holds project-level instructions."""

    def __init__(self, text: str = "Follow repository conventions.") -> None:
        self.text = text
