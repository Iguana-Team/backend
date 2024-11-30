from pydantic import BaseModel
from src.dto.user_dto import UserDTO
from src.enums import UserPermissionEnum


class RegisterUserRequest(BaseModel):
    id: int
    username: str
    password: str
    permission: UserPermissionEnum
