class StaffPublicDTO:
    id: int
    phone: int
    city: str
    address: str
    mail: str

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.phone = kwargs.get('phone')
        self.city = kwargs.get('city')
        self.address = kwargs.get('address')
        self.mail = kwargs.get('mail')

    def to_dict(self) -> dict:
        return self.__dict__;

    @classmethod
    def from_dict(user: StaffPrivateDTO, data: dict) -> StaffPrivateDTO: # type: ignore
        return user(**data)
