from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient()
db = client.lexscan

async def get_history(user_id: str):
    return await db.history.find({"user_id": user_id}).to_list()

async def delete_history(user_id: str):
    return await db.history.delete_many({"user_id": user_id})