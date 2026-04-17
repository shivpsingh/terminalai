"""Tool schema models."""

from pydantic import BaseModel


class FilePathInput(BaseModel):
    """Input model for tools with path argument."""

    path: str
