from src.enums import UserPermissionEnum
from hashlib import sha256

class UserDTO:
    id: int
    username: str
    password: str
    permission: UserPermissionEnum

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.username = kwargs.get('username')
        self.password = hash(sha256(kwargs.get('password')).hexdigest())
        self.permission = kwargs.get('permission')

    def to_dict(self) -> dict:
        return self.__dict__;

    @staticmethod
    def is_eq_users(lhs: UserDTO, rhs: UserDTO) -> bool: # type: ignore
        return lhs.to_dict() == rhs.to_dict()
