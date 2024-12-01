from dataclasses import dataclass
from pydantic import BaseModel
from src.enums import FuncBlockEnum, Division4Enum, RoleEnum

@dataclass
class StaffPublicRequest:
    id: int
    func_block: FuncBlockEnum
    division1: str
    division2: str
    division3: str
    division4: Division4Enum
    post: str
    role: RoleEnum
    lname: str
    fname: str

@dataclass
class StaffPrivateRequest:
    username: str
    password: str
    staff_id: str
