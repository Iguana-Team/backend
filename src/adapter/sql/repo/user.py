from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable
from contextlib import AbstractAsyncContextManager
from datetime import date, datetime
from src.enums import UserPermissionEnum
from src.interface.repo.user import Sta


class UserRepository(UserRepositoryInterface):
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]):
        self.session_factory = session_factory


    async def add_user(self, username: str, password: str, permission: UserPermissionEnum):
        async with self.session_factory() as session:
            new_user = User(user_id=user_id, user_type=user_type, user_class=user_class)
            session.add(new_user)
            await session.commit()

    async def is_user_exist(self, username: str, password: str, permission: UserPermissionEnum):
        pass
