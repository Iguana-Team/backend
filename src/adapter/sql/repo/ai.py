from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from typing import Callable, Optional, List
from contextlib import AbstractAsyncContextManager
from src.dto.staff_public_dto import StaffPublicDTO
from src.service.ai.service import NearestNeighborsModel

from os import walk

class AIModelRepository:
    model: NearestNeighborsModel

    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory
        self.model = NearestNeighborsModel


    async def match_staff(self, staff: StaffPublicDTO) -> List[StaffPublicDTO]:
        return self.model.find_nearest_neighbors(staff)


    async def get_model(self):
        files = next(walk('/app'), (None, None, []))[2]
        if 'model.pkl' in files:
            self.model = NearestNeighborsModel.load_model('model.pkl')
        else:
            async with self.session_factory() as session:
                data = await session.execute(select(StaffPublicDTO))
                self.model = NearestNeighborsModel(data.scalars())
                self.model.fit()

Ы