from staff import User
from src.enums import UserPermissionEnum

class UserDTO:
    id: int
    username: str
    password: str
    permission: UserPermissionEnum

    def __init__(self, id: str, username: str, password: str, permission: UserPermissionEnum) -> None:
        self.id = id
        self.username = username
        self.permission = permission

    def to_dict(self) -> dict:
        return self.__dict__;

    @classmethod
    def from_dict(user: UserDTO, data: dict) -> UserDTO: # type: ignore
        return user(**data)

    @staticmethod
    def is_eq_users(lhs: UserDTO, rhs: UserDTO) -> bool: # type: ignore
        return lhs.to_dict() == rhs.to_dict()
