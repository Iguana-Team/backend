from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()


POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class Database:
    url: str
    engine: AsyncEngine
    session: async_sessionmaker

    def __init__(self):
        self.url = DATABASE_URL
        self.engine = create_async_engine(self.url, echo=False)
        self.session = async_sessionmaker(bind=self.engine)

    @asynccontextmanager
    async def session(self) -> AsyncSession:
        session: AsyncSession = self.session()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
