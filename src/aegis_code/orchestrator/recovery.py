"""Recovery and retry helpers."""

import asyncio
from collections.abc import Awaitable, Callable


async def retry_async(
    operation: Callable[[], Awaitable[object]],
    retries: int = 2,
) -> object:
    """Retry transient async operations."""

    attempts = 0
    while True:
        try:
            return await operation()
        except Exception:  # noqa: BLE001
            attempts += 1
            if attempts > retries:
                raise
            await asyncio.sleep(0)
