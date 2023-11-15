"""added the fk constraints between trainer profile and organization

Revision ID: fdb506138ee5
Revises: 021fc32810ee
Create Date: 2023-11-14 19:58:43.381482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdb506138ee5'
down_revision: Union[str, None] = '021fc32810ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        'fk_trainer_profile_organization',
        'trainer_profile_id',
        'trainer'
    )
    # op.create_foreign_key(
    #     'organization',
    #     ''
    # )


def downgrade() -> None:
    pass