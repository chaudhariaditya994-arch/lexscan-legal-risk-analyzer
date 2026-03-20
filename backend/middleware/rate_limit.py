from __future__ import annotations

from collections import defaultdict, deque
from datetime import UTC, datetime, timedelta

from fastapi import HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)
_request_windows: dict[str, deque[datetime]] = defaultdict(deque)


def _max_requests(plan: str) -> int:
    return 30 if plan == "pro" else 10


async def enforce_plan_rate_limit(request: Request | None, user_plan: str = "free") -> None:
    address = get_remote_address(request) if request is not None else "local"
    key = f"{address}:{user_plan}"
    now = datetime.now(UTC)
    window = _request_windows[key]
    cutoff = now - timedelta(hours=1)

    while window and window[0] < cutoff:
        window.popleft()

    if len(window) >= _max_requests(user_plan):
        raise HTTPException(status_code=429, detail="Rate limit exceeded for the current plan.")

    window.append(now)
