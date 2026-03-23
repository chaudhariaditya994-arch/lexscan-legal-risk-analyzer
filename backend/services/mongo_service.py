from motor.motor_asyncio import AsyncIOMotorClient
import datetime

client = AsyncIOMotorClient()
db = client.lexscan

async def get_history(user_id: str):
    return await db.history.find({"user_id": user_id}).to_list()

async def delete_history(user_id: str):
    return await db.history.delete_many({"user_id": user_id})

async def save_analysis(user_id: str, analysis: dict):
    await db.history.insert_one({"user_id": user_id, "analysis": analysis, "timestamp": datetime.datetime.utcnow()})