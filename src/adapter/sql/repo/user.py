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


    async def add_message(self, user_id: str, content: dict):
        async with self.session_factory() as session:
            message = Message(user_id=user_id, content=content)
            session.add(message)
            await session.commit()


    async def get_chat_history(self, user_id: str, n: int, offset: int = 0) -> Optional[Sequence[Message]]:
        async with self.session_factory() as session:
            result = await session.execute(select(User).filter_by(user_id=user_id))
            user = result.scalars().first()
            if not user:
                return
            result = await session.execute(
                select(Message).filter_by(user_id=user.user_id).order_by(Message.id.desc()).offset(offset).limit(n)
            )
            return result.scalars().all()


    async def get_today_messages(self, user_id: str) -> Optional[Sequence[Message]]:
        async with self.session_factory() as session:
            result = await session.execute(select(User).filter_by(user_id=user_id))
            user = result.scalars().first()
            if not user:
                return

            today = date.today()
            result = await session.execute(
                select(Message)
                .filter(
                    and_(
                        Message.user_id == user.user_id,
                        func.date(Message.timestamp) == today
                    )
                )
                .order_by(Message.id.desc())
            )
            return result.scalars().all()


    async def get_allowed_tokens(self, user_type: str) -> Optional[int]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(UserType).filter_by(user_type=user_type)
            )
            user_type_model = result.scalars().first()
            if user_type_model:
                return user_type_model.allowed_tokens
            return


    async def get_user(self, user_id: str) -> Optional[UserDTO]:
        async with self.session_factory() as session:
            result = await session.execute(select(User).filter_by(user_id=user_id))
            user = result.scalars().first()
            if user:
                user_dto = UserDTO(
                    id=user.id,
                    user_id=user.user_id,
                    user_type=user.user_type,
                    user_class=user.user_class,
                    created_at=user.created_at
                )
                return user_dto
            return
