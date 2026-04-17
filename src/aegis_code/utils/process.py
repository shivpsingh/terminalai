"""Process helpers."""

import subprocess


def run_command(args: list[str], cwd: str = ".") -> subprocess.CompletedProcess[str]:
    """Run a command and capture output."""

    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)
