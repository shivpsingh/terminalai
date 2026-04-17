"""Tool runtime composition."""

from __future__ import annotations

from aegis_code.policy.engine import PolicyEngine
from aegis_code.tools.builtins.edit_file import EditFileTool
from aegis_code.tools.builtins.git_diff import GitDiffTool
from aegis_code.tools.builtins.git_status import GitStatusTool
from aegis_code.tools.builtins.read_file import ReadFileTool
from aegis_code.tools.builtins.run_shell import RunShellTool
from aegis_code.tools.builtins.run_tests import RunTestsTool
from aegis_code.tools.builtins.search_files import SearchFilesTool
from aegis_code.tools.builtins.web_lookup import WebLookupTool
from aegis_code.tools.builtins.write_file import WriteFileTool
from aegis_code.tools.executor import EventRepository, ToolExecutor
from aegis_code.tools.registry import ToolRegistry


def build_registry() -> ToolRegistry:
    """Register built-in tools."""

    registry = ToolRegistry()
    for tool in [
        ReadFileTool(),
        WriteFileTool(),
        EditFileTool(),
        SearchFilesTool(),
        RunShellTool(),
        GitStatusTool(),
        GitDiffTool(),
        RunTestsTool(),
        WebLookupTool(),
    ]:
        registry.register(tool)
    return registry


def build_executor(event_repo: EventRepository) -> ToolExecutor:
    """Create executor with default policy."""

    return ToolExecutor(build_registry(), PolicyEngine(), event_repo)
