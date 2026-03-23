from motor.motor_asyncio import AsyncIOMotorClient
import datetime
import os

client = AsyncIOMotorClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/lexscan"))
db = client.lexscan

async def get_history(user_id: str):
    cursor = db.history.find({"user_id": user_id})
    return await cursor.to_list(length=None)

async def delete_history(user_id: str):
    result = await db.history.delete_many({"user_id": user_id})
    return {"deleted_count": result.deleted_count}

async def save_analysis(user_id: str, analysis: dict):
    document = {
        "user_id": user_id,
        "analysis": analysis,
        "timestamp": datetime.datetime.now(datetime.timezone.utc)
    }
    result = await db.history.insert_one(document)
    return {"inserted_id": str(result.inserted_id)}