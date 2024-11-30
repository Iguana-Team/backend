from dataclasses import dataclass

@dataclass
class StaffPrivateDTO:
    id: int
    phone: int
    city: str
    address: str
    mail: str
