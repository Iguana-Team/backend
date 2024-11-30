from dataclasses import dataclass
from pydantic import BaseModel
from src.enums import UserPermissionEnum


@dataclass
class SingUpUserRequest(BaseModel):
    id: int
    username: str
    password: str
    permission: UserPermissionEnum


@dataclass
class LoginUserRequest(BaseModel):
    id: int
    username: str
    password: str
    permission: UserPermissionEnum
