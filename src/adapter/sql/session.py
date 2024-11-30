from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker


class Database:
    url: str
    engine: AsyncEngine
    session: async_sessionmaker


    def __init__(self, url: str):
        self.url = url
        self.engine = create_async_engine(url, echo=False)
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
