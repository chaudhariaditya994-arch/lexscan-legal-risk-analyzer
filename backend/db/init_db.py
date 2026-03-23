from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient()
db = client.lexscan

async def init_db():
    # create indexes
    pass