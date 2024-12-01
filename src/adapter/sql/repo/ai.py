from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from typing import Callable, Optional
from contextlib import AbstractAsyncContextManager
from src.adapter.sql.models import AI
from src.dto.staff_public_dto import StaffPublicDTO


class AIModelRepository:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory

    async def match_staff(self, user: StaffPublicDTO) -> bool:
        async with self.session_factory() as session:
            # processing

            return # List< StaffPublicDTO >
