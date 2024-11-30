from src.enums import UserPermissionEnum
from hashlib import sha256
from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    username: str
    password: str
    permission: UserPermissionEnum
