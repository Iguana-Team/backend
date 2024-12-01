from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from typing import Callable, Optional
from contextlib import AbstractAsyncContextManager
from src.adapter.sql.models import AI


class AIModelRepository:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory

    async def load_model(self, model_id: int) -> Optional[AI]:
        async with self.session_factory() as session:
            result = await session.execute(select(AI).filter_by(id=model_id))
            return result.scalars().first()

    async def get_latest_model(self) -> Optional[AI]:
        async with self.session_factory() as session:
            result = await session.execute(select(AI).order_by(desc(AI.created_at)))
            return result.scalars().first()
