from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable
from contextlib import AbstractAsyncContextManager
from src.dto.user_dto import UserDTO

class UserRepository():
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory


    async def add_user(self, rhs: UserDTO) -> None:
        async with self.session_factory() as session:
            await session.commit()

    async def is_user_exist(self, rhs: UserDTO) -> None:
        pass
