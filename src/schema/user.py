from dataclasses import dataclass
from pydantic import BaseModel
from src.enums import UserPermissionEnum


@dataclass
class SingUpUserRequest(BaseModel):
    username: str
    password: str
    permission: UserPermissionEnum


@dataclass
class LoginUserRequest(BaseModel):
    username: str
    password: str
