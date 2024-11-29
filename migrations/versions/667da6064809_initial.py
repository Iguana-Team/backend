from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '667da6064809'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with open("mtslink.sql", "r") as mtslink:
        op.execute(mtslink.read())

    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('password', sa.String(length=50), nullable=False),
        # sa.Column('permission', sa.Enum)
    )


def downgrade():
    op.drop_table('staff_public')
    op.drop_table('staff_private')
    op.drop_table('users')
