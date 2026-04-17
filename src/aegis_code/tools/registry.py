"""Tool registry."""

from aegis_code.tools.base import BaseTool


class ToolRegistry:
    """In-process registry keyed by tool name."""

    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """Register a tool instance."""

        self._tools[tool.metadata.name] = tool

    def get(self, name: str) -> BaseTool:
        """Fetch registered tool."""

        return self._tools[name]

    def list_names(self) -> list[str]:
        """List known tool names."""

        return sorted(self._tools)
