from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import Text, and_, func
from src.adapter.sql.models.user import User, Message, UserType, TokenTransaction
from typing import Callable, Optional, Sequence, List, Tuple
from contextlib import AbstractAsyncContextManager
from datetime import date, datetime
from src.enums.user_class import  UserClassEnum
from src.enums.user_type import UserTypeEnum
from src.dto.user import UserDTO
from src.interface.repo.user import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]):
        self.session_factory = session_factory


    async def add_user(self, user_id: str, user_type: UserTypeEnum, user_class: UserClassEnum | None = None):
        async with self.session_factory() as session:
            new_user = User(user_id=user_id, user_type=user_type, user_class=user_class)
            session.add(new_user)
            await session.commit()
