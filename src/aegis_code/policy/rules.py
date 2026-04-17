"""Policy rule helpers."""

from pathlib import Path


def within_workspace(path: str, workspace_root: str) -> bool:
    """Ensure path stays under workspace root."""

    root = Path(workspace_root).resolve()
    target = Path(path).resolve()
    return str(target).startswith(str(root))
