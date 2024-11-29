from sqlalchemy import Column, Integer, String, BigInteger
from src.adapter.sql.base import Base


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, autoincrement=True)
    division1 = Column(String(50))
    functional = Column(String(50))
    division2 = Column(String(100))
    division3 = Column(String(50))
    division4 = Column(String(50))
    post = Column(String(50))
    role = Column(String(50))
    lname = Column(String(50))
    fname = Column(String(50))
    phone = Column(BigInteger)
    city = Column(String(50))
    address = Column(String(100))
    mail = Column(String(100))
