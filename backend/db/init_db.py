from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/lexscan"))
db = client.lexscan

async def init_db():
    # Create indexes for better performance
    await db.history.create_index("user_id")
    await db.history.create_index("timestamp")
    await db.history.create_index([("user_id", 1), ("timestamp", -1)])
    
    # Ensure collections exist
    collections = await db.list_collection_names()
    if "history" not in collections:
        await db.create_collection("history")
    
    print("Database initialized successfully")