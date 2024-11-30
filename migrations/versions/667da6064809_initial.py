from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import json
from sqlalchemy.sql import table, column

revision: str = '667da6064809'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


func_block_enum = postgresql.ENUM(
    'Корпоративный блок', 'Розничный блок', "", name="funcblockenum")

division4_enum = postgresql.ENUM('Дополнительный офис 1', 'Дополнительный офис 2',
                                 'Дополнительный офис 3', 'Дополнительный офис 4', "", name="division4enum")

role_enum = postgresql.ENUM('руководство', 'Дизайнер', 'аналитика', 'backend',
                            'frontend', 'тестирование', 'бэк-офис', 'продажи', 'обслуживание', name="roleenum")

user_permission_enum = postgresql.ENUM(
    'user', 'admin', name="userpermissionenum")


def upgrade():
    op.create_table(
        'staff_public',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('func_block', func_block_enum, nullable=False),
        sa.Column('division1', sa.String(100), nullable=False),
        sa.Column('division2', sa.String(100), nullable=False),
        sa.Column('division3', sa.String(100), nullable=False),
        sa.Column('division4', division4_enum, nullable=False),

        sa.Column('post', sa.String(100), nullable=False),
        sa.Column('role', role_enum, nullable=False),
        sa.Column('lname', sa.String(100), nullable=False),
        sa.Column('fname', sa.String(100), nullable=False),
    )

    op.create_table(
        'staff_private',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('phone', sa.BigInteger(), nullable=False),
        sa.Column('city', sa.String(100), nullable=False),
        sa.Column('address', sa.String(300), nullable=False),
        sa.Column('mail', sa.String(100), nullable=False),
    )

    staff_private_table = table(
        'staff_private',
        column('id', sa.Integer),
        column('phone', sa.BigInteger),
        column('city', sa.String),
        column('address', sa.String),
        column('mail', sa.String),
    )

    staff_public_table = table(
        'staff_public',
        column('id', sa.Integer),
        column('func_block', func_block_enum),
        column('division1', sa.String),
        column('division2', sa.String),
        column('division3', sa.String),
        column('division4', division4_enum),
        column('post', sa.String),
        column('role', role_enum),
        column('lname', sa.String),
        column('fname', sa.String),
    )

    with open('staff_public.json', 'r') as public_data:
        data_public = json.load(public_data)
    op.bulk_insert(
        staff_public_table,
        data_public
    )

    with open('staff_private.json', 'r') as mtslink_data:
        data = json.load(mtslink_data)
    op.bulk_insert(
        staff_private_table,
        data
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(length=100), nullable=False),
        sa.Column('password', sa.String(length=100), nullable=False),
        sa.Column('permission', user_permission_enum, nullable=False)
    )


def downgrade():
    op.drop_table('staff_public')
    op.drop_table('staff_private')
    op.drop_table('users')
