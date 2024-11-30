from typing import Sequence, Union
from alembic.op import execute, create_table, drop_table
from sqlalchemy import Column, String, Integer, Enum
import enum

revision: str = '667da6064809'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

class UserPermissionEnum(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'

def upgrade():
    with open("mtslink.sql", "r") as mtslink:
        execute(mtslink.read())

    create_table(
        'users',
        Column('id', Integer(), nullable=False, autoincrement=True),
        Column('username', String(length=50), nullable=False),
        Column('password', String(length=50), nullable=False),
        Column('permission', Enum(UserPermissionEnum), nullable=False)
    )


def downgrade():
    drop_table('staff_public')
    drop_table('staff_private')
    drop_table('users')
