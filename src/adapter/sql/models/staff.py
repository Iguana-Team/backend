from sqlalchemy import Column, Integer, String, BigInteger, Enum
from src.adapter.sql.base import Base
from enums import FuncBlockEnum, Division4Enum, RoleEnum, UserPermissionEnum


class StaffPublic(Base):
    __tablename__ = 'staff_public'

    id = Column(Integer, primary_key=True, autoincrement=True)
    func_block = Column(Enum(FuncBlockEnum), nullable=False)
    division1 = Column(String(100), nullable=False)
    division2 = Column(String(100), nullable=False)
    division3 = Column(String(100), nullable=False)
    division4 = Column(Enum(Division4Enum), nullable=False)
    post = Column(String(100), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    lname = Column(String(100), nullable=False)
    fname = Column(String(100), nullable=False)

class StaffPrivate(Base):
    __tablename__ = 'staff_private'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(BigInteger, nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(300), nullable=False)
    mail = Column(String(100), nullable=False)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=50), nullable=False),
    password = Column(String(length=50), nullable=False),
    permission = Column(Enum(UserPermissionEnum), nullable=False)

