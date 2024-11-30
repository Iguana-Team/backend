from src.enums import FuncBlockEnum, Division4Enum, RoleEnum


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

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.func_block = kwargs.get('func_block')
        self.division1 = kwargs.get('division1')
        self.division2 = kwargs.get('division2')
        self.division3 = kwargs.get('division3')
        self.division4 = kwargs.get('division4')
        self.post = kwargs.get('post')
        self.role = kwargs.get('role')
        self.lname = kwargs.get('lname')
        self.fname = kwargs.get('rname')

    def to_dict(self) -> dict:
        return self.__dict__
