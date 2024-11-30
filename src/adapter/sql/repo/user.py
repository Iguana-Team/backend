from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable
from contextlib import AbstractAsyncContextManager
from src.enums import UserPermissionEnum


class UserRepository():
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]):
        self.session_factory = session_factory


    async def add_user(self, username: str, password: str, permission: UserPermissionEnum):
        async with self.session_factory() as session:
            await session.commit()

    async def is_user_exist(self, username: str, password: str, permission: UserPermissionEnum):
        pass
