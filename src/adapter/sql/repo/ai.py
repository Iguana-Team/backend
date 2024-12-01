from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from typing import Callable, Optional, List
from contextlib import AbstractAsyncContextManager
from src.dto.staff_public_dto import StaffPublicDTO
from src.service.ai.service import NearestNeighborsModel
from src.adapter.sql.models.staff import StaffPublic

from src.enums import FuncBlockEnum, Division4Enum, RoleEnum
from os import walk

class AIModelRepository:
    model: NearestNeighborsModel

    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory
        self.model = None
        self.is_ready = False        


    async def match_staff(self, staff: StaffPublicDTO) -> list:
        await self.get_model()
        if self.is_ready:
            tmp = self.model.find_nearest_neighbors(staff)
            if not tmp:
                return [StaffPublicDTO(2, FuncBlockEnum.CORPORATE, 'sad', 'assd', 'asd', Division4Enum.OFFICE2, 'sada', 'asda','asdas', 'asd')]
            return tmp


    async def get_model(self) -> None:
        files = next(walk('/app'), (None, None, []))[2]
        if 'model.pkl' in files:
            self.model = NearestNeighborsModel.load_model('model.pkl')
        else:
            async with self.session_factory() as session:
                data = await session.execute(select(StaffPublic))
                self.model = NearestNeighborsModel(data.scalars().all())
                self.model.fit()
        self.is_ready = True
