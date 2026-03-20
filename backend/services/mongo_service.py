from __future__ import annotations

import os
from collections import defaultdict
from typing import Any
from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorClient


class MongoService:
    def __init__(self) -> None:
        self.uri = os.getenv("MONGODB_URI", "")
        self.database_name = os.getenv("MONGODB_DATABASE", "lexscan")
        self._client: AsyncIOMotorClient | None = None
        self._db = None
        self._memory_history: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._memory_by_id: dict[str, dict[str, Any]] = {}

    async def connect(self) -> None:
        if not self.uri:
            return
        self._client = AsyncIOMotorClient(self.uri)
        self._db = self._client[self.database_name]

    async def disconnect(self) -> None:
        if self._client is not None:
            self._client.close()

    async def init_indexes(self) -> None:
        if self._db is None:
            return
        await self._db.analyses.create_index("userId")
        await self._db.analyses.create_index("pdfHash")

    async def insert_analysis(self, user_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        stored = {**payload, "id": str(uuid4()), "userId": user_id}
        if self._db is not None:
            await self._db.analyses.insert_one(stored)
            return stored
        self._memory_history[user_id].insert(0, stored)
        self._memory_by_id[stored["id"]] = stored
        return stored

    async def list_history(self, user_id: str) -> list[dict[str, Any]]:
        if self._db is not None:
            cursor = self._db.analyses.find({"userId": user_id}).sort("_id", -1)
            return await cursor.to_list(length=100)
        return list(self._memory_history.get(user_id, []))

    async def delete_history(self, user_id: str) -> int:
        if self._db is not None:
            result = await self._db.analyses.delete_many({"userId": user_id})
            return result.deleted_count
        deleted = len(self._memory_history.get(user_id, []))
        for item in self._memory_history.get(user_id, []):
            self._memory_by_id.pop(item["id"], None)
        self._memory_history[user_id] = []
        return deleted

    async def get_analysis(self, analysis_id: str) -> dict[str, Any] | None:
        if self._db is not None:
            return await self._db.analyses.find_one({"id": analysis_id})
        return self._memory_by_id.get(analysis_id)


mongo_service = MongoService()
