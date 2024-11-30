from src.enums import UserPermissionEnum
from dataclasses import dataclass
import hashlib

@dataclass
class UserDTO:
    id: int
    username: str
    password: str
    permission: UserPermissionEnum

def is_user_valid(lhs: UserDTO, rhs: UserDTO) -> bool:
    return lhs.username == rhs.username and lhs.password == rhs.password

def process_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
