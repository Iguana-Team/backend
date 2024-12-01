from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Callable, Optional
from contextlib import AbstractAsyncContextManager
from src.dto.staff_public_dto import StaffPublicDTO
from src.dto.staff_private_dto import StaffPrivateDTO
from src.dto.user_dto import UserDTO, is_user_valid
from src.service.ai.service import NearestNeighborsModel
from src.adapter.sql.models.staff import StaffPublic, StaffPrivate, Users
from src.enums import UserPermissionEnum
from os import walk


class AIModelRepository:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory
        self.model = None
        self.is_ready = False        


    async def match_staff(self, staff: StaffPublicDTO) -> list:
        if not self.is_ready:
            await self.get_model()
        return self.model.find_nearest_neighbors(staff) 


    async def get_private_info(self, user: UserDTO, staff_id: int) -> StaffPrivateDTO:
        perm = await self.get_permission(user)
        if perm == UserPermissionEnum.USER:
            return StaffPrivateDTO(staff_id, 0, '', '', '')
        if perm == UserPermissionEnum.ADMIN:
            async with self.session_factory() as session:
                tmp = await session.execute(select(StaffPrivate).filter_by(id=staff_id))
                tmp = tmp.scalars().first()
                return StaffPrivateDTO(tmp.id, tmp.phone, tmp.city, tmp.address, tmp.mail)

        return StaffPrivateDTO(staff_id, 0, perm.value, '', '')


    async def get_permission(self, user: UserDTO) -> UserPermissionEnum:
        tmp = await self.find_user(user)
        if not await self.is_user_exists(tmp):
            return UserPermissionEnum.USER
        return tmp.permission if is_user_valid(user, tmp) else UserPermissionEnum.USER


    async def is_user_exists(self, user: UserDTO) -> bool:
        if user is None:
            return False
        return await self.find_user(user) is not None


    async def find_user(self, user: UserDTO) -> Optional[UserDTO]:
        if user is None:
            return None
        async with self.session_factory() as session:
            tmp = await session.execute(select(Users).filter_by(username=user.username))
            return tmp.scalars().first()


    async def get_model(self) -> None:
        files = next(walk('/app'), (None, None, []))[2]
        if 'model.pkl' in files:
            self.model = NearestNeighborsModel.load_model('model.pkl')
        else:
            async with self.session_factory() as session:
                data = await session.execute(select(StaffPublic))
                self.model = NearestNeighborsModel(data.scalars().all())
                self.model.fit()
                self.model.save_model('/app/model.pkl')
        self.is_ready = True
