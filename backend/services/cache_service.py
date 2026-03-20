from __future__ import annotations

import json
import os
from hashlib import sha256
from typing import Any

from redis.asyncio import Redis


class CacheService:
    def __init__(self) -> None:
        self.redis_url = os.getenv("REDIS_URL", "")
        self.ttl_seconds = 86400
        self._redis: Redis | None = None
        self._memory: dict[str, dict[str, Any]] = {}

    async def connect(self) -> None:
        if not self.redis_url:
            return
        self._redis = Redis.from_url(self.redis_url, decode_responses=True)

    async def disconnect(self) -> None:
        if self._redis is not None:
            await self._redis.aclose()

    @staticmethod
    def build_pdf_hash(file_bytes: bytes) -> str:
        return sha256(file_bytes).hexdigest()

    def _key(self, pdf_hash: str) -> str:
        return f"lexscan:analysis:{pdf_hash}"

    async def get(self, pdf_hash: str) -> dict[str, Any] | None:
        key = self._key(pdf_hash)
        if self._redis is not None:
            value = await self._redis.get(key)
            return json.loads(value) if value else None
        return self._memory.get(key)

    async def set(self, pdf_hash: str, payload: dict[str, Any]) -> None:
        key = self._key(pdf_hash)
        if self._redis is not None:
            await self._redis.set(key, json.dumps(payload), ex=self.ttl_seconds)
            return
        self._memory[key] = payload


cache_service = CacheService()
