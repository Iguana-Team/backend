from src.adapter.sql.base import Base
from sqlalchemy import Column, Integer, LargeBinary, TIMESTAMP, func
from datetime import datetime


class AI(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(LargeBinary)
    created_at = Column(TIMESTAMP, default=datetime.utcnow,
                        server_default=func.now())
