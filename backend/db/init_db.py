from services.mongo_service import mongo_service


async def init_db() -> None:
    await mongo_service.connect()
    await mongo_service.init_indexes()
