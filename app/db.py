import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from app.config import settings

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:
    def __init__(self):
        self.__session = None
        self.__engine = None

    def connect(self, db_config):
        self.__engine = create_async_engine(settings.DB_URI)
        self.__session = async_sessionmaker(bind=self.__engine, autocommit=False)

    async def disconnect(self):
        await self.__engine.dispose()

    async def get_db(self):
        async with self.__session() as session:
            yield session


db = Database()
