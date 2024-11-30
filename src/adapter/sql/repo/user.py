from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Callable, Optional
from contextlib import AbstractAsyncContextManager
from src.dto.user_dto import UserDTO
from src.adapter.sql.models.staff import Users
import hashlib


class UserRepository():
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory


    async def singup(self, user: UserDTO) -> bool:
        async with self.session_factory() as session:
            if await self.is_user_exists(user):
                return False
            
            new_user = Users(
                id=user.id,
                username=user.username,
                password=user.password,
                permission=user.permission)
            session.add(new_user)
            await session.commit()

            return True
        

    async def login(self, user: UserDTO) -> bool:
        tmp = await self.is_user_exists(user)
        if UserDTO.is_eq_users(user, tmp):
            return True
        return False


    async def is_user_exists(self, user: UserDTO) -> Optional[UserDTO]:
        async with self.session_factory() as session:
            tmp = await session.execute(select(Users).filter_by(username=user.username))
            return tmp.scalars().first()

