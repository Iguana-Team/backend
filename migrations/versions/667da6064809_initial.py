"""initial

Revision ID: 667da6064809
Revises: 
Create Date: 2024-11-29 21:46:25.689647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '667da6064809'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'staff',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('division1', sa.String(length=50), nullable=True),
        sa.Column('functional', sa.String(length=50), nullable=True),
        sa.Column('division2', sa.String(length=100), nullable=True),
        sa.Column('division3', sa.String(length=50), nullable=True),
        sa.Column('division4', sa.String(length=50), nullable=True),
        sa.Column('post', sa.String(length=50), nullable=True),
        sa.Column('role', sa.String(length=50), nullable=True),
        sa.Column('lname', sa.String(length=50), nullable=True),
        sa.Column('fname', sa.String(length=50), nullable=True),
        sa.Column('phone', sa.BigInteger(), nullable=True),
        sa.Column('city', sa.String(length=50), nullable=True),
        sa.Column('address', sa.String(length=100), nullable=True),
        sa.Column('mail', sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('staff')
