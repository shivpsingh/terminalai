"""ID factories."""

from uuid import uuid4


def _new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:12]}"


def new_run_id() -> str:
    return _new_id("run")


def new_task_id() -> str:
    return _new_id("task")


def new_step_id() -> str:
    return _new_id("step")


def new_checkpoint_id() -> str:
    return _new_id("ckpt")
