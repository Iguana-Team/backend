from typing import Sequence, Union
from alembic.op import execute, create_table, drop_table
from sqlalchemy import Column, String, Integer

from enum import Enum as python_enum_t
from sqlalchemy import Enum as sql_enum_t

revision: str = '667da6064809'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class FuncBlockEnum(python_enum_t):
    CORPORATE = 'Корпоративный блок'
    RETAIL = 'Розничный блок'


class Division4Enum(python_enum_t):
    OFFICE1 = 'Дополнительный офис 1'
    OFFICE2 = 'Дополнительный офис 2'
    OFFICE3 = 'Дополнительный офис 3'
    OFFICE4 = 'Дополнительный офис 4'


class RoleEnum(python_enum_t):
    LEADERSHIP = 'руководство'
    DESIGNER = 'Дизайнер'
    ANALYST = 'аналитика'
    BACKEND = 'backend'
    FRONTEND = 'frontend'
    TESTER = 'тестирование'
    BACKOFFICE = 'бэк-офис'
    SALES = 'продажи'
    SERVICE = 'обслуживание'


class UserPermissionEnum(python_enum_t):
    USER = 'user'
    ADMIN = 'admin'


def upgrade():
    create_table(
        'staff_public',
        Column('id', Integer(), primary_key=True, autoincrement=True),
        Column('func_block', sql_enum_t(FuncBlockEnum), nullable=False),
        Column('division1', String(100), nullable=False),
        Column('division2', String(100), nullable=False),
        Column('division3', String(100), nullable=False),
        Column('division4', sql_enum_t(Division4Enum), nullable=False),

        Column('post', String(100), nullable=False),
        Column('role', sql_enum_t(RoleEnum), nullable=False),
        Column('lname', String(100), nullable=False),
        Column('fname', String(100), nullable=False),
    )

    create_table(
        'staff_private',
        Column('id', Integer(), primary_key=True, autoincrement=True),
        Column('phone', Integer(), nullable=False),
        Column('city', String(100), nullable=False),
        Column('address', String(300), nullable=False),
        Column('mail', String(100), nullable=False),
    )

    with open('processed_mtslink.sql', 'r') as mtslink_data:
        execute(mtslink_data.read())

    create_table(
        'users',
        Column('id', Integer(), primary_key=True, autoincrement=True),
        Column('username', String(length=100), nullable=False),
        Column('password', String(length=100), nullable=False),
        Column('permission', python_enum_t(UserPermissionEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    )


def downgrade():
    drop_table('staff_public')
    drop_table('staff_private')
    drop_table('users')
