"""Sandbox policy settings."""

from pydantic import BaseModel


class SandboxPolicy(BaseModel):
    """Sandbox boundaries for tool execution."""

    workspace_root: str = "."
    allow_network: bool = False
