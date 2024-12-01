from sqlalchemy import Column, Integer, BINARY, TIMESTAMP
from src.adapter.sql.base import Base


class StaffPublic(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(BINARY)
    created_at = Column(TIMESTAMP)
