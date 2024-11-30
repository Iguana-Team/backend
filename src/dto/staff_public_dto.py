from src.enums import FuncBlockEnum, Division4Enum, RoleEnum
from dataclasses import dataclass


@dataclass
class StaffPublicDTO:
    id: int
    func_block: FuncBlockEnum
    division1: str
    division2: str
    division3: str
    division4 = Division4Enum
    post: str
    role: RoleEnum
    lname: str
    fname: str
