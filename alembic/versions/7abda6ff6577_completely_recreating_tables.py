"""completely_recreating_tables

Revision ID: 7abda6ff6577
Revises: 139e272cd86e
Create Date: 2023-12-27 20:32:51.471411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7abda6ff6577'
down_revision: Union[str, None] = '139e272cd86e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(255), nullable=False),
    sa.Column('last_name', sa.String(255), nullable=True),
    sa.Column('display_name', sa.String(255), nullable=True),
    sa.Column('email', sa.String(255), nullable=False),
    sa.Column('password', sa.String(500), nullable=False),
    sa.Column('upldate', sa.DateTime(), nullable=False),
    sa.Column('moddate', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('email')
    )

def downgrade() -> None:
    op.drop_table('user')
