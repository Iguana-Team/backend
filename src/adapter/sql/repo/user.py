from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable
from contextlib import AbstractAsyncContextManager
from src.dto.user_dto import UserDTO
from src.adapter.sql.models.staff import Users
import hashlib


class UserRepository():
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]) -> None:
        self.session_factory = session_factory

    async def add_user(self, user: UserDTO) -> None:
        async with self.session_factory() as session:
            new_user = Users(
                id=user.id,
                username=user.username,
                password=hash(hashlib.sha256(user.password).hexdigest()),
                permission=user.permission)
            session.add(new_user)
            await session.commit()

    async def is_user_exist(self, user: UserDTO) -> None:
        pass
