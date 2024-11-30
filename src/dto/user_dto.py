from src.enums import UserPermissionEnum
from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    username: str
    password: str
    permission: UserPermissionEnum
