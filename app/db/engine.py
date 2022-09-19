from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
engine = AIOEngine(client=client)
