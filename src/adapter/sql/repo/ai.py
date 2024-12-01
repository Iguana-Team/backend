from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from typing import Callable, Optional, List
from contextlib import AbstractAsyncContextManager
from src.adapter.sql.models import AI
from src.dto.staff_public_dto import StaffPublicDTO
from src.service.ai.service import NearestNeighborsModel


class AIModelRepository:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory

    async def model_fit(self, data: List[StaffPublicDTO]):
        async with self.session_factory() as session:
            # получаем всю бд
            # обучаем через fit()
            # опционально: сохранить обученную модель (NearestNeighborsModel.save_model())
            pass

    async def match_staff(self, user: StaffPublicDTO):
        async with self.session_factory() as session:
            # берём нужные данные и используем NearestNeighborsModel.find_nearest_neighbors()
            # чтобы получить результат

            return # List< StaffPublicDTO >
