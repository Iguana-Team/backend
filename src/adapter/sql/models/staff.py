from sqlalchemy import Column, Integer, String, BigInteger, Enum
from src.adapter.sql.base import Base
from src.enums import UserPermissionEnum


class StaffPublic(Base):
    __tablename__ = 'staff_public'

    id = Column(Integer, primary_key=True, autoincrement=True)
    func_block = Column(String(100), nullable=False)
    division1 = Column(String(100), nullable=False)
    division2 = Column(String(100), nullable=False)
    division3 = Column(String(100), nullable=False)
    division4 = Column(String(100), nullable=False)
    post = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    lname = Column(String(100), nullable=False)
    fname = Column(String(100), nullable=False)


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "func_block": self.func_block,
            "division1": self.division1,
            "division2": self.division2,
            "division3": self.division3,
            "division4": self.division4,
            "post": self.post,
            "role": self.role,
            "lname": self.lname,
            "fname": self.fname
        }


class StaffPrivate(Base):
    __tablename__ = 'staff_private'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(BigInteger, nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(300), nullable=False)
    mail = Column(String(100), nullable=False)


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "phone": self.phone,
            "city": self.city,
            "address": self.city,
            "mail": self.mail
        }


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=100), nullable=False)
    password = Column(String(length=100), nullable=False)
    permission = Column(Enum(UserPermissionEnum), nullable=False)
